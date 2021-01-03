from configs.config import ApplicationConfig
from context import Context
from transport.sanic import endpoints


def get_routes(config: ApplicationConfig, context: Context) -> tuple:
    return (
        endpoints.HealthEndpoint(config=config, context=context, uri='/', methods=('GET', 'POST')),
        endpoints.CreateUserEndpoint(config=config, context=context, uri='/user', methods=['POST']),
        endpoints.GetUserEndpoint(config=config, context=context, uri='/user', methods=['GET']),
    )
