from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request import RequestCreateMessageDto, RequestGetMessageDto
from api.response.message import ResponseCreateMessageDto, ResponseGetMessageDto
from db.database import DBSession
from db.models import DBMessage
from db.queries import message as message_queries
from transport.sanic.endpoints import BaseEndpoint


class MessageEndpoint(BaseEndpoint):

    async def method_post(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestCreateMessageDto(body)

        db_message = message_queries.create_message(session, request_model)
        session.commit_session()

        response_model = ResponseCreateMessageDto(db_message)

        return await self.make_response_json(body=response_model.dump(), status=201)

    async def method_get(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestGetMessageDto(body)

        db_messages = message_queries.get_messages(session, request_model)
        db_content_messages = [GetMes(mes.content_message) for mes in db_messages]

        session.commit_session()

        # db_message = DBMessage(content_message='assa')
        response_model = ResponseGetMessageDto(db_content_messages)
        # GetMes('fsdfsd')
        return await self.make_response_json(body=response_model.dump(), status=200)

class GetMes:
    def __init__(self, messages):
        self.messages = messages
