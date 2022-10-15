### Yandex SmartCapcha

1. Клонировать эту репу
2. Зарегистировать свою капчу согласно доке https://cloud.yandex.ru/docs/smartcaptcha/quickstart#creat-captcha и взять оттуда ключи для клиента и сервера
3. Создать файл `.env` в корне проекта:
```
SMARTCAPTCHA_CLIENT_KEY=your-client-key
SMARTCAPTCHA_SERVER_KEY=your-server-key
```
4. `npm install` (нужна установленная nodejs)
5. `npm start`
6. На `http://localhost:3000/` будет страница с редиректами на капчу-чекбокс и невидимую капчу
