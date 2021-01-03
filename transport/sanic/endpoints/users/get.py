from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request import RequestGetUserDto
from api.response import ResponseUserDto, ResponseGetUserDto
from db.database import DBSession
from transport.sanic.endpoints import BaseEndpoint
from db.queries import user as user_queries


class GetUserEndpoint(BaseEndpoint):
    async def method_get(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestGetUserDto(body)

        db_user = user_queries.get_user(session, request_model)
        print(db_user.login)
        session.commit_session()

        response_model = ResponseGetUserDto(db_user)

        return await self.make_response_json(body=response_model.dump(), status=201)
