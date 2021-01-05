from sqlalchemy import Column, VARCHAR, Integer, ForeignKey

from db.models import BaseModel


class DBMessage(BaseModel):

    __tablename__ = 'messages'

    id_sender = Column(
        Integer,
        ForeignKey('users.id'),
        nullable=False,
    )
    id_recipient = Column(
        Integer,
        ForeignKey('users.id'),
        nullable=False,
    )
    content_message = Column(VARCHAR(4096))
