import pytest

from db.models import DBUser
from helpers.password import generate_hash
from transport.sanic.endpoints import CreateUserEndpoint, UserEndpoint


@pytest.mark.asyncio
async def test_post_user_endpoint(request_factory, patched_context, mocker):
    password = 'qwerty'
    hsh_ = generate_hash(password)

    json_data = {
        'login': 'lex123',
        'password': password,
        'first_name': 'Alexey',
        'last_name': 'Dorin',
    }

    request = request_factory(
        method='post',
        content_type='application/json',
        json=json_data
    )

    db_user = DBUser(
        id=1,
        login=json_data['login'],
        first_name=json_data['first_name'],
        last_name=json_data['last_name'],
        password=hsh_
    )
    patched_query = mocker.patch('db.queries.user.create_user')
    patched_query.return_value = db_user

    endpoint = CreateUserEndpoint(None, patched_context, '/user', ['POST'])
    response = await endpoint(request)

    assert response.status == 201


@pytest.mark.asyncio
async def test_get_user_endpoint(request_factory, patched_context, request_header_authorization, mocker):
    password = 'qwerty'
    hsh_ = generate_hash(password)

    request = request_factory(
        method='get',
        headers=request_header_authorization
    )

    db_user = DBUser(
        id=1,
        login='lex123',
        first_name='Alexey',
        last_name='Dorin',
        password=hsh_
    )
    patched_query = mocker.patch('db.queries.user.get_user')
    patched_query.return_value = db_user

    endpoint = UserEndpoint(None, patched_context, '/user/1', ['GET'], auth_required=True)
    response = await endpoint(request, uid=1)

    assert response.status == 200


@pytest.mark.asyncio
async def test_patch_user_endpoint(request_factory, patched_context, request_header_authorization, mocker):
    password = 'qwerty'
    hsh_ = generate_hash(password)
    db_user = DBUser(
        id=1,
        login='lex123',
        first_name='Alexei',
        last_name='Dori',
        password=hsh_
    )
    json_data = {
        'first_name': 'Lech',
        'last_name': 'Dorin',
    }

    request = request_factory(
        method='patch',
        headers=request_header_authorization,
        content_type='application/json',
        json=json_data
    )

    patched_query = mocker.patch('db.queries.user.get_user')
    patched_query.return_value = db_user

    db_user.first_name = json_data['first_name']
    db_user.last_name = json_data['last_name']

    patched_query = mocker.patch('db.queries.user.patch_user')
    patched_query.return_value = db_user

    endpoint = UserEndpoint(None, patched_context, '/user/1', ['PATCH'], auth_required=True)
    response = await endpoint(request, uid=1)

    assert response.status == 200
