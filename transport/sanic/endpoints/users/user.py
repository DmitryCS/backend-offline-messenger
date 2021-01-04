from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request import RequestCreateUserDto, RequestGetUserDto, RequestPatchUserDto
from api.response import ResponseCreateUserDto, ResponseGetUserDto
from api.response.user import ResponsePatchUserDto
from db.database import DBSession
from transport.sanic.endpoints import BaseEndpoint

from db.queries import user as user_queries


class UserEndpoint(BaseEndpoint):

    async def method_get(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestGetUserDto(body)

        db_user = user_queries.get_user(session, request_model)

        session.commit_session()

        response_model = ResponseGetUserDto(db_user)

        return await self.make_response_json(body=response_model.dump(), status=200)

    async def method_post(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestCreateUserDto(body)

        db_user = user_queries.create_user(session, request_model)
        session.commit_session()

        response_model = ResponseCreateUserDto(db_user)

        return await self.make_response_json(body=response_model.dump(), status=201)

    async def method_patch(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestPatchUserDto(body)

        db_user = user_queries.patch_user(session, request_model)
        session.commit_session()

        response_model = ResponsePatchUserDto(db_user)

        return await self.make_response_json(body=response_model.dump(), status=200)
