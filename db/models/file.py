from sqlalchemy import Column, VARCHAR, Integer, ForeignKey, BOOLEAN

from db.models import BaseModel


class DBFile(BaseModel):

    __tablename__ = 'files'

    sender_id = Column(
        Integer,
        ForeignKey('users.id'),
        nullable=False,
    )
    ref_file = Column(
        VARCHAR(4096)
    )
    is_delete = Column(
        BOOLEAN(),
        nullable=False,
        default=False
    )
