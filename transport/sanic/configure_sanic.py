from sanic import Sanic

from transport.sanic.routes import get_routes


def configure_app():
    app = Sanic(__name__)

    for handler in get_routes():
        app.add_route(
            handler=handler,
            uri=handler.uri,
            methods=handler.methods,
            strict_slashes=True,
        )

    return app
