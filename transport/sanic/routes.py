from configs.config import ApplicationConfig
from context import Context
from transport.sanic import endpoints


def get_routes(config: ApplicationConfig, context: Context) -> tuple:
    return (
        endpoints.HealthEndpoint(
            config=config, context=context, uri='/', methods=['GET']
        ),
        endpoints.CreateUserEndpoint(
            config=config, context=context, uri='/user', methods=['POST']
        ),
        endpoints.AuthUserEndpoint(
            config, context, uri='/auth', methods=['POST']
        ),
        endpoints.UserEndpoint(
            config, context, uri='/user/<uid:int>', methods=('GET', 'PATCH'),
            auth_required=True
        ),
        endpoints.MessagesEndpoint(
            config=config, context=context, uri='/msg', methods=('GET', 'POST'),
            auth_required=True
        ),
        endpoints.MessageEndpoint(
            config=config, context=context, uri='/msg/<message_id:int>', methods=('GET', 'PATCH', 'DELETE'),
            auth_required=True
        ),
    )
