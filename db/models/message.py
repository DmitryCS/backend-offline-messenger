from sqlalchemy import Column, VARCHAR, Integer, ForeignKey, BOOLEAN

from db.models import BaseModel


class DBMessage(BaseModel):

    __tablename__ = 'messages'

    sender_id = Column(
        Integer,
        ForeignKey('users.id'),
        nullable=False,
    )
    recipient_id = Column(
        Integer,
        ForeignKey('users.id'),
        nullable=False,
    )
    message = Column(
        VARCHAR(4096)
    )
    is_delete = Column(
        BOOLEAN(),
        nullable=False,
        default=False
    )
