from sqlalchemy import Column, VARCHAR, Integer, ForeignKey, BOOLEAN

from db.models import BaseModel


class DBMsgFile(BaseModel):

    __tablename__ = 'msgs_to_files'

    msg_id = Column(
        Integer,
        ForeignKey('messages.id'),
        nullable=False,
    )
    file_id = Column(
        Integer,
        ForeignKey('files.id'),
        nullable=False,
    )
    is_delete = Column(
        BOOLEAN(),
        nullable=False,
        default=False
    )
