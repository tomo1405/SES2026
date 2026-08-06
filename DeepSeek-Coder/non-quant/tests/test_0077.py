import pytest
from src_0077 import task_func
from unittest.mock import patch
from django.http import HttpResponse

@pytest.fixture
def mock_request():
    class MockRequest:
        def __init__(self):
            self.session = {}
    return MockRequest()

@pytest.mark.parametrize("session_expire_time, expected_status_code", [
    (3600, 200),
    (7200, 200)
])
def test_task_func(mock_request, session_expire_time, expected_status_code):
    with patch('src_0077.random.choices', return_value='mocked_session_key'):
        response = task_func(mock_request, session_expire_time)
        assert response.status_code == expected_status_code