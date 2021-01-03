from sqlalchemy import Column, VARCHAR

from db.models import BaseModel


class DBUser(BaseModel):

    __tablename__ = 'users'

    first_name = Column(VARCHAR(50))
    last_name = Column(VARCHAR(50))
    login = Column(VARCHAR(50))
    password = Column(VARCHAR(100))
