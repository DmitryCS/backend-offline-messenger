import pytest

from db.models import DBMessage
from transport.sanic.endpoints.messages.messages import MessagesEndpoint


@pytest.mark.asyncio
async def test_all_messages_endpoint(request_factory, patched_context, request_header_authorization, mocker):
    patched_query = mocker.patch('db.queries.message.get_messages')
    patched_query.return_value = []

    request = request_factory(
        method='get',
        headers=request_header_authorization
    )
    endpoint = MessagesEndpoint(None, patched_context, '/msg', ['GET'], auth_required=True)
    response = await endpoint(request)

    assert response.status == 200


@pytest.mark.asyncio
async def test_post_messages_endpoint(request_factory, patched_context, request_header_authorization, mocker):
    new_message = DBMessage(
        id=1,
        sender_id=1,
        recipient_id=2,
        message="message",
    )

    patched_query = mocker.patch('db.queries.message.create_message')
    patched_query.return_value = new_message

    json_data = {
        'recipient': 'lex123',
        'message': 'Hello, lex123.'
    }

    request = request_factory(
        method='post',
        content_type='application/json',
        headers=request_header_authorization,
        json=json_data
    )

    endpoint = MessagesEndpoint(None, patched_context, '/msg', ['POST'], auth_required=True)
    response = await endpoint(request)

    assert response.status == 201
