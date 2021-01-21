from typing import List

from api.request import RequestCreateMessageDto, RequestGetMessageDto
from db.database import DBSession
from db.models import DBUser
from db.models.message import DBMessage


def create_message(session: DBSession, request_dto_message: RequestCreateMessageDto, user_id: int) -> DBMessage:
    recipient = session.get_user_by_login(request_dto_message.recipient)

    new_message = DBMessage(
        sender_id=user_id,
        recipient_id=recipient.id,
        message=request_dto_message.message,
    )

    session.add_model(new_message)

    return new_message


def get_messages(session: DBSession, user_id: int) -> List[DBMessage]:

    list_messages = session.get_all_messages(user_id) #session.query(DBMessage).filter_by(id_recipient=5).all()

    return list_messages
