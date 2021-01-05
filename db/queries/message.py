from typing import List

from api.request import RequestCreateMessageDto, RequestGetMessageDto
from db.database import DBSession
from db.models import DBUser
from db.models.message import DBMessage


def create_message(session: DBSession, message: RequestCreateMessageDto) -> DBMessage:
    recipient = session.query(DBUser).filter_by(login=message.recipient).first().id

    new_message = DBMessage(
        id_sender=4,
        id_recipient=recipient,
        content_message=message.message,
    )

    session.add_model(new_message)

    return new_message


def get_messages(session: DBSession, message: RequestGetMessageDto) -> List[DBMessage]:

    list_messages = session.query(DBMessage).filter_by(id_recipient=5).all()

    return list_messages
