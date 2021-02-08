from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request import RequestCreateMessageDto
from api.response.message import ResponseCreateMessageDto, ResponseGetMessageDto
from db.database import DBSession
from db.exceptions import (
    DBUserNotExistsException,
    DBDataException,
    DBIntegrityException,
    DBFileNotExistsException,
    DBResourceOwnerException
)
from db.queries import message as message_queries
from db.queries import file as file_queries
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import (
    SanicUserNotFound,
    SanicDBException,
    SanicFileNotFound,
    SanicUserConflictException
)


class MessagesEndpoint(BaseEndpoint):

    async def method_post(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestCreateMessageDto(body)
        try:
            message = message_queries.create_message(session, request_model, body['uid'])
        except DBUserNotExistsException:
            raise SanicUserNotFound('Recipient not found')

        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        try:
            if hasattr(request_model, 'file_ids'):
                for file_id in request_model.file_ids:
                    file_queries.create_msg_file_relation(
                        session=session,
                        user_id=body['uid'],
                        msg_id=message.id,
                        file_id=file_id
                    )
        except DBFileNotExistsException:
            raise SanicFileNotFound('File not found')
        except DBResourceOwnerException:
            raise SanicUserConflictException("This is not your file")

        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))
        message.file_ids = []
        if hasattr(request_model, 'file_ids'):
            message.file_ids = request_model.file_ids
        response_model = ResponseCreateMessageDto(message)

        return await self.make_response_json(body=response_model.dump(), status=201)

    async def method_get(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:

        db_messages = message_queries.get_messages(session, body['uid'])
        for message in db_messages:
            message.file_ids = file_queries.get_file_ids_by_msd_id(session, message.id)
        response_model = ResponseGetMessageDto(db_messages, many=True)

        return await self.make_response_json(body=response_model.dump(), status=200)
