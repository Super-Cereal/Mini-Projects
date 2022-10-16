const pointOfView = require("point-of-view");
const ejs = require("ejs");

module.exports = {
  configureFastify: () => {
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
    fastify.register(pointOfView, { engine: { ejs }, templates: "./templates" });

    return fastify;
  },
};
