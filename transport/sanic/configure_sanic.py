from sanic import Sanic
from sanic_openapi import swagger_blueprint

from configs.config import ApplicationConfig
from context import Context
from hooks import init_db_sqlite
from transport.sanic.routes import get_routes


def configure_app(config: ApplicationConfig, context: Context):

    init_db_sqlite(config, context)

    app = Sanic(__name__)
    app.blueprint(swagger_blueprint)

    for handler in get_routes(config, context):
        app.add_route(
            handler=handler,
            uri=handler.uri,
            methods=handler.methods,
            strict_slashes=True,
        )

    return app
