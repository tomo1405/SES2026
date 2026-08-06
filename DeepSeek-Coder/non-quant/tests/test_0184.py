import pytest
from src_0184 import task_func
from unittest.mock import patch
import uuid
from django.http import HttpResponse

def test_task_func():
    # Mock the UUID generation
    with patch('uuid.uuid4', return_value=uuid.uuid4()):
        response = task_func("test_data")
        assert isinstance(response, HttpResponse)
        assert response.content == b"test_data"
        assert response['UUID'] is not None
        assert 'UUID' in response