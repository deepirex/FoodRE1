import os
import json
import pytest
import sys
from pathlib import Path
from flask import Flask

# Add the project root to the Python path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

@pytest.fixture
def client():
    app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'))
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_response(client):
    result = client.get()
    response_body = result.get_data()
    print(response_body)
    assert result.status_code == 200
