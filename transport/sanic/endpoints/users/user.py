from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request import RequestGetUserDto, RequestPatchUserDto
from api.response import ResponseGetUserDto
from api.response.user import ResponsePatchUserDto
from db.database import DBSession
from db.exceptions import DBUserExistsException, DBDataException, DBIntegrityException, DBUserNotExistsException
from helpers.password import generate_hash, GeneratePasswordHashException
from transport.sanic.endpoints import BaseEndpoint

from db.queries import user as user_queries
from transport.sanic.exceptions import SanicPasswordHashException, SanicUserConflictException, SanicDBException, \
    SanicUserNotFound


class UserEndpoint(BaseEndpoint):

    async def method_get(self, request: Request, body: dict, session: DBSession, uid: int, *args, **kwargs) -> BaseHTTPResponse:

        user = user_queries.get_user(session, user_id=uid)

        session.commit_session()

        response_model = ResponseGetUserDto(user)

        return await self.make_response_json(body=response_model.dump(), status=200)

    async def method_patch(self, request: Request, body: dict, session: DBSession, uid: int, *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestPatchUserDto(body)
        try:
            user = user_queries.patch_user(session, request_model, uid)
        except DBUserNotExistsException:
            raise SanicUserNotFound('User not found')
        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        response_model = ResponsePatchUserDto(user)

        return await self.make_response_json(body=response_model.dump(), status=200)
