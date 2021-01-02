from transport.sanic import endpoints


def get_routes() -> tuple:
    return (
        endpoints.HealthEndpoint(uri='/', methods=('GET', 'POST')),
    )
