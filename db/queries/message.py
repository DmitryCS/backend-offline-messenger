from typing import List

from api.request import RequestCreateMessageDto, RequestGetMessageDto
from api.request.message import RequestPatchMessageDto
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

    list_messages = session.get_all_messages(user_id)

    return list_messages


def patch_message(session: DBSession, request_dto_message: RequestPatchMessageDto, message_id: int) -> DBMessage:

    db_message = session.get_message_by_id(message_id)

    for attr in request_dto_message.fields:
        value = getattr(request_dto_message, attr)
        setattr(db_message, attr, value)

    return db_message


def delete_message(session: DBSession, message_id: int) -> None:

    db_message = session.get_message_by_id(message_id)
    db_message.is_delete = True


def get_message(session: DBSession, message_id: int) -> DBMessage:

    message = session.get_message(message_id)

    return message
