const querystring = require("querystring");
const https = require("https");

const { SMARTCAPTCHA_SERVER_KEY } = require("../constants");

module.exports = {
  checkCapcha: (request) => {
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

    return new Promise((resolve) => {
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
  },
};
