import json
import pytest
from application import application


@pytest.fixture
def client():
    return application.test_client()


def test_response(client):
    result = client.get()
    response_body = result.get_data()
    print(response_body)
    assert result.status_code == 200