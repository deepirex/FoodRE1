import json
import pytest
import sys
from pathlib import Path

# Add the project root to the Python path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from application import application

# Rest of the test code
@pytest.fixture
def client():
    return application.test_client()


def test_response(client):
    result = client.get()
    response_body = result.get_data()
    print(response_body)
    assert result.status_code == 200