const { SMARTCAPTCHA_CLIENT_KEY } = require("../constants");

const { checkCapcha } = require("../controllers/check-capcha");

module.exports = {
  registerRoutes: (fastify) => {
    // отдаем темплейты клиента
    fastify.get("/", (_, reply) => {
      reply.view("client-redirect-page.ejs");
    });

    fastify.get("/1", (_, reply) => {
      console.log('SMARTCAPTCHA_CLIENT_KEY', SMARTCAPTCHA_CLIENT_KEY);
      reply.view("client-checkbox-capcha.ejs", {
        capchaClientKey: SMARTCAPTCHA_CLIENT_KEY,
      });
    });
    fastify.post("/1", (req) => {
      const { name, password } = req.body;
      return `форма 1 отправлена, name: ${name}, password: ${password}`;
    });

    fastify.get("/2", (_, reply) => {
      reply.view("client-invisible-capcha.ejs", {
        capchaClientKey: SMARTCAPTCHA_CLIENT_KEY,
      });
    });
    fastify.post("/2", (req) => {
      const { name, password } = req.body;
      return `форма 2 отправлена, name: ${name}, password: ${password}`;
    });

    // проверяем капчу на сервере яндекса
    fastify.get("/check-capcha", checkCapcha);
  },
};
