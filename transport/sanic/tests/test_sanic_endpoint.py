import pytest

from transport.sanic.base import SanicEndpoint


@pytest.mark.asyncio
async def test_valid_method_called(request_factory):
    request = request_factory(method='get')

    endpoint = SanicEndpoint(None, None, '', ())

    response = await endpoint(request)

    assert response.status == 500
