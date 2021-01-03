from configs.config import ApplicationConfig
from context import Context
from transport.sanic import endpoints


def get_routes(config: ApplicationConfig, context: Context) -> tuple:
    return (
        endpoints.HealthEndpoint(config=config, context=context, uri='/', methods=('GET', 'POST')),
    )