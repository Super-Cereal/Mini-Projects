// зависимости для рендера клиента
const { registerRoutes } = require("./routes/routes");
const { configureFastify } = require("./configure-fastify");

// настроили сервер
const fastify = configureFastify();
registerRoutes(fastify);

// запустили сервер на порту 3000
fastify.listen({ port: 3000 }, function (err, address) {
  if (err) {
    fastify.log.error(err);
    process.exit(1);
  }
  console.log(`Server is now listening on ${address}`);
});
