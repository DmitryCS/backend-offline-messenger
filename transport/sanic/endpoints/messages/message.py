from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request.message import RequestPatchMessageDto
from api.response.message import ResponsePatchMessageDto, ResponseGetMessageDto
from db.database import DBSession
from db.exceptions import (
    DBMessageNotExistsException,
    DBDataException,
    DBIntegrityException,
    DBResourceOwnerException,
    DBFileNotExistsException,
    DBMsgFileNotExistsException
)
from db.queries import message as message_queries
from db.queries import file as file_queries
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import (
    SanicMessageNotFound,
    SanicDBException,
    SanicUserConflictException,
    SanicFileNotFound
)


class MessageEndpoint(BaseEndpoint):

    async def method_patch(
            self, request: Request, body: dict, session: DBSession, message_id: int, *args, **kwargs
    ) -> BaseHTTPResponse:

        request_model = RequestPatchMessageDto(body)

        try:
            message = message_queries.patch_message(session, request_model, message_id, body['uid'])
        except DBMessageNotExistsException:
            raise SanicMessageNotFound('Message not found')
        except DBResourceOwnerException:
            raise SanicUserConflictException("This is not your message")

        try:
            if hasattr(request_model, 'file_ids'):
                file_ids = file_queries.get_file_ids_by_msd_id(session, message_id)
                file_ids_merged = list(set(file_ids + request_model.file_ids))
                for file_id in file_ids_merged:
                    if file_id not in file_ids:
                        file_queries.create_msg_file_relation(
                            session=session,
                            user_id=body['uid'],
                            msg_id=message_id,
                            file_id=file_id
                        )
                    elif file_id not in request_model.file_ids:
                        file_queries.delete_msg_file_relation(
                            session=session,
                            user_id=body['uid'],
                            msg_id=message_id,
                            file_id=file_id
                        )
        except DBFileNotExistsException:
            raise SanicFileNotFound('File not found')
        except DBMsgFileNotExistsException:
            raise SanicFileNotFound('MsgFile not found')
        except DBResourceOwnerException:
            raise SanicUserConflictException("This is not your file")

        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        message.file_ids = file_queries.get_file_ids_by_msd_id(session, message.id)
        response_model = ResponsePatchMessageDto(message)

        return await self.make_response_json(body=response_model.dump(), status=200)

    async def method_delete(
            self, request: Request, body: dict, session: DBSession, message_id: int, *args, **kwargs
    ) -> BaseHTTPResponse:
        file_ids = file_queries.get_file_ids_by_msd_id(session, message_id)

        try:
            for file_id in file_ids:
                file_queries.delete_msg_file_relation(session, body['uid'], message_id, file_id)
        except DBMsgFileNotExistsException:
            raise SanicFileNotFound('File not found')
        except DBResourceOwnerException:
            raise SanicUserConflictException("This is not your message")

        try:
            message_queries.delete_message(session, message_id, body['uid'])
        except DBMessageNotExistsException:
            raise SanicMessageNotFound('Message not found')
        except DBResourceOwnerException:
            raise SanicUserConflictException("This is not your message")

        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        return await self.make_response_json(status=204)

    async def method_get(
            self, request: Request, body: dict, session: DBSession, message_id: int, *args, **kwargs
    ) -> BaseHTTPResponse:

        try:
            message = message_queries.get_message(session, message_id)
        except DBMessageNotExistsException as e:
            raise SanicDBException(str(e))
        if message.recipient_id != body['uid']:
            raise SanicUserConflictException("This message is not for you")

        message.file_ids = file_queries.get_file_ids_by_msd_id(session, message.id)
        response_model = ResponseGetMessageDto(message)

        return await self.make_response_json(body=response_model.dump(), status=200)
