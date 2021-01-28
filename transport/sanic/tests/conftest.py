import pytest
import sqlalchemy

from context import Context
from db.database import (
    DataBase,
    DBSession,
)
from helpers.auth import create_token


@pytest.fixture()
def request_factory():

    class Request:
        def __init__(
                self,
                method: str = 'get',
                content_type: str = '',
                headers: dict = None,
                json: str = None,
        ):
            self.method = method.upper()
            self.content_type = content_type
            self.headers = headers or {}
            self.json = json

    return Request


@pytest.fixture()
def patched_context(patched_db) -> Context:
    context = Context()
    context.set('database', patched_db)

    return context


@pytest.fixture()
def patched_db(mocker):
    patched_engine = mocker.patch.object(sqlalchemy, 'create_engine')
    patched_engine.return_value = None

    patched_make_session = mocker.patch.object(DataBase, 'make_session')
    patched_make_session.return_value = DBSession(session=None)

    patched_commit_session = mocker.patch.object(DBSession, 'commit_session')
    patched_commit_session.return_value = None

    return DataBase


@pytest.fixture()
def request_header_authorization():
    payload = {
        'uid': 1,
    }
    header = {
        'Authorization': create_token(payload)
    }
    return header
