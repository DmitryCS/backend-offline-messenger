from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request import RequestPatchUserDto
from api.response import ResponseGetUserDto
from api.response.user import ResponsePatchUserDto
from db.database import DBSession
from db.exceptions import DBDataException, DBIntegrityException, DBUserNotExistsException
from transport.sanic.endpoints import BaseEndpoint

from db.queries import user as user_queries
from transport.sanic.exceptions import SanicUserConflictException, SanicDBException, SanicUserNotFound


class UserEndpoint(BaseEndpoint):

    async def method_get(
            self, request: Request, body: dict, session: DBSession, uid: int, *args, **kwargs
    ) -> BaseHTTPResponse:

        if body['uid'] != uid:
            raise SanicUserConflictException("This is not your user")
        try:
            user = user_queries.get_user(session, user_id=uid)
        except DBUserNotExistsException:
            raise SanicUserNotFound('User not found')

        response_model = ResponseGetUserDto(user)

        return await self.make_response_json(body=response_model.dump(), status=200)

    async def method_patch(
            self, request: Request, body: dict, session: DBSession, uid: int, *args, **kwargs
    ) -> BaseHTTPResponse:

        if body['uid'] != uid:
            raise SanicUserConflictException("This is not your user")

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
