from configs.config import ApplicationConfig
from context import Context
from transport.sanic import endpoints


def get_routes(config: ApplicationConfig, context: Context) -> tuple:
    return (
        endpoints.HealthEndpoint(config=config, context=context, uri='/', methods=['GET']),
        endpoints.UserEndpoint(config=config, context=context, uri='/user', methods=('GET', 'POST', 'PATCH')),
        endpoints.MessageEndpoint(config=config, context=context, uri='/msg', methods=('GET', 'POST')),
    )
