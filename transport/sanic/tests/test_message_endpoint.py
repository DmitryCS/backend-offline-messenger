import pytest

from db.models import DBMessage
from transport.sanic.endpoints import MessageEndpoint


@pytest.mark.asyncio
async def test_get_message_endpoint(request_factory, patched_context, request_header_authorization, mocker):
    new_message = DBMessage(
        id=1,
        sender_id=2,
        recipient_id=1,
        message="message",
    )
    patched_query = mocker.patch('db.queries.message.get_message')
    patched_query.return_value = new_message
    patched_query = mocker.patch('db.queries.file.get_file_ids_by_msd_id')
    patched_query.return_value = []

    request = request_factory(
        method='get',
        headers=request_header_authorization
    )
    endpoint = MessageEndpoint(None, patched_context, '/msg/1', ['GET'], auth_required=True)
    response = await endpoint(request, message_id=1)

    assert response.status == 200


@pytest.mark.asyncio
async def test_patch_message_endpoint(request_factory, patched_context, request_header_authorization, mocker):
    new_message = DBMessage(
        id=1,
        sender_id=1,
        recipient_id=2,
        message="message",
    )

    patched_query = mocker.patch('db.queries.message.patch_message')
    patched_query.return_value = new_message
    patched_query = mocker.patch('db.queries.file.get_file_ids_by_msd_id')
    patched_query.return_value = []

    json_data = {
        'message': 'Hello, lex123.'
    }

    request = request_factory(
        method='patch',
        content_type='application/json',
        headers=request_header_authorization,
        json=json_data
    )

    endpoint = MessageEndpoint(None, patched_context, '/msg/1', ['PATCH'], auth_required=True)
    response = await endpoint(request, message_id=1)

    assert response.status == 200


@pytest.mark.asyncio
async def test_delete_message_endpoint(request_factory, patched_context, request_header_authorization, mocker):
    patched_query = mocker.patch('db.queries.file.get_file_ids_by_msd_id')
    patched_query.return_value = []
    patched_query = mocker.patch('db.queries.message.delete_message')
    patched_query.return_value = None

    request = request_factory(
        method='delete',
        headers=request_header_authorization,
    )

    endpoint = MessageEndpoint(None, patched_context, '/msg/1', ['DELETE'], auth_required=True)
    response = await endpoint(request, message_id=1)

    assert response.status == 204
