const querystring = require("querystring");
const https = require("https");

// зависимости для рендера клиента
const pointOfView = require("point-of-view");
const ejs = require("ejs");

require("dotenv").config();
const SMARTCAPTCHA_SERVER_KEY = process.env.SMARTCAPTCHA_SERVER_KEY;
const SMARTCAPTCHA_CLIENT_KEY = process.env.SMARTCAPTCHA_CLIENT_KEY;

// настроили сервер
const fastify = require("fastify")({
  logger: {
    transport: {
      target: "pino-pretty",
      options: {
        ignore: "pid,hostname",
      },
    },
  },
});
fastify.register(require("@fastify/formbody"));
fastify.register(pointOfView, { engine: { ejs } });

// отдаем клиент
fastify.get("/", (_, reply) => {
  reply.view("./client-redirect-page.ejs");
});
fastify.get("/1", (_, reply) => {
  reply.view("./client-checkbox-capcha.ejs", {
    capchaClientKey: SMARTCAPTCHA_CLIENT_KEY,
  });
});
fastify.post("/1", (req) => {
  const { name, password } = req.body;
  return `форма 1 отправлена, name: ${name}, password: ${password}`;
});
fastify.get("/2", (_, reply) => {
  reply.view("./client-invisible-capcha.ejs", {
    capchaClientKey: SMARTCAPTCHA_CLIENT_KEY,
  });
});
fastify.post("/2", (req) => {
  const { name, password } = req.body;
  return `форма 2 отправлена, name: ${name}, password: ${password}`;
});

// проверяем капчу на сервере яндекса
fastify.get("/check-capcha", (request) => {
  const { token } = request.query;

  const options = {
    hostname: "captcha-api.yandex.ru",
    port: 443,
    path:
      "/validate?" +
      querystring.stringify({
        secret: SMARTCAPTCHA_SERVER_KEY,
        token: token,
        ip: request.ip, // Способ получения IP-адреса пользователя зависит от вашего фреймворка и прокси.
      }),
    method: "GET",
  };

  const result = new Promise((resolve) => {
    const req = https.request(options, (res) => {
      res.on("data", (content) => {
        if (res.statusCode !== 200) {
          console.error(
            `Allow access due to an error: code=${res.statusCode}; message=${content}`
          );
          resolve(true);
          return;
        }
        resolve(JSON.parse(content).status === "ok");
      });
    });
    req.on("error", (error) => {
      console.error(error);
      resolve(true);
    });
    req.end();
  });

  return result;
});

// запустили сервер на порту 3000
fastify.listen({ port: 3000 }, function (err, address) {
  if (err) {
    fastify.log.error(err);
    process.exit(1);
  }
  console.log(`Server is now listening on ${address}`);
});
