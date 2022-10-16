require("dotenv").config();
const SMARTCAPTCHA_SERVER_KEY = process.env.SMARTCAPTCHA_SERVER_KEY;
const SMARTCAPTCHA_CLIENT_KEY = process.env.SMARTCAPTCHA_CLIENT_KEY;

if (!SMARTCAPTCHA_CLIENT_KEY || !SMARTCAPTCHA_SERVER_KEY) {
  console.log('!!! НЕТ .env ФАЙЛА С ЗАДАННЫМИ КЛЮЧАМИ - КАПЧА НЕ БУДЕТ РАБОТАТЬ !!!')
}

module.exports = {
  SMARTCAPTCHA_SERVER_KEY,
  SMARTCAPTCHA_CLIENT_KEY,
};
