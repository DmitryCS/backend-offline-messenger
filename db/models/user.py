from sqlalchemy import Column, VARCHAR, LargeBinary

from db.models import BaseModel


class DBUser(BaseModel):

    __tablename__ = 'users'

    first_name = Column(VARCHAR(50))
    last_name = Column(VARCHAR(50))
    login = Column(VARCHAR(50), unique=True, nullable=False)
    password = Column(LargeBinary(), nullable=False)
