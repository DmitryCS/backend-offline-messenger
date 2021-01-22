from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request.message import RequestPatchMessageDto
from api.response.message import ResponsePatchMessageDto, ResponseGetMessageDto
from db.database import DBSession
from db.exceptions import DBMessageNotExistsException, DBDataException, DBIntegrityException
from db.queries import message as message_queries
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicMessageNotFound, SanicDBException, SanicUserConflictException


class MessageEndpoint(BaseEndpoint):

    async def method_patch(
            self, request: Request, body: dict, session: DBSession, message_id: int, *args, **kwargs
    ) -> BaseHTTPResponse:

        request_model = RequestPatchMessageDto(body)

        try:
            message = message_queries.patch_message(session, request_model, message_id, body['uid'])
        except DBMessageNotExistsException:
            raise SanicMessageNotFound('Message not found')

        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        response_model = ResponsePatchMessageDto(message)

        return await self.make_response_json(body=response_model.dump(), status=200)

    async def method_delete(
            self, request: Request, body: dict, session: DBSession, message_id: int, *args, **kwargs
    ) -> BaseHTTPResponse:

        try:
            message_queries.delete_message(session, message_id, body['uid'])
        except DBMessageNotExistsException as e:
            raise SanicDBException(str(e))

        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        return await self.make_response_json(status=204)

    async def method_get(
            self, request: Request, body: dict, session: DBSession, message_id: int, *args, **kwargs
    ) -> BaseHTTPResponse:

        db_message = message_queries.get_message(session, message_id)

        if db_message is None:
            raise SanicMessageNotFound('Message not found')

        if body['uid'] not in (db_message.sender_id, db_message.recipient_id):
            raise SanicUserConflictException("This is not your message")

        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        response_model = ResponseGetMessageDto(db_message)

        return await self.make_response_json(body=response_model.dump(), status=200)
