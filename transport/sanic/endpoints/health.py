from sanic.request import Request
from sanic.response import BaseHTTPResponse

from transport.sanic.base import SanicEndpoint


class HealthEndpoint(SanicEndpoint):

    async def method_get(self, request: Request, body: dict,  *args, **kwargs) -> BaseHTTPResponse:
        response = {
            'hello': 'world'
        }
        return await self.make_response_json(body=response, status=200)