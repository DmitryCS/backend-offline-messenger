import pytest

from db.models import DBUser
from helpers.password import generate_hash
from transport.sanic.endpoints import AuthUserEndpoint


@pytest.mark.asyncio
async def test_post_auth_endpoint(request_factory, patched_context, mocker):
    password = 'qwerty'
    hsh_ = generate_hash(password)
    db_user = DBUser(
        id=1,
        login='lex123',
        password=hsh_
    )
    patched_query = mocker.patch('db.queries.user.get_user')
    patched_query.return_value = db_user

    json_data = {
        'login': 'lex123',
        'password': password
    }

    request = request_factory(
        method='post',
        content_type='application/json',
        json=json_data
    )

    endpoint = AuthUserEndpoint(None, patched_context, '/auth', ['POST'])
    response = await endpoint(request)

    assert response.status == 200
