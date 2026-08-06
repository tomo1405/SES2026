import pytest
from django.http import HttpResponse
from src_0184 import task_func
import uuid

def test_task_func():
    # Test data
    data = '{"key": "value"}'

    # Call the function
    response = task_func(data)

    # Check if the response is an instance of HttpResponse
    assert isinstance(response, HttpResponse)

    # Check if the content type is 'application/json'
    assert response['Content-Type'] == 'application/json'

    # Check if the response content is the same as the input data
    assert response.content.decode('utf-8') == data

    # Check if the UUID header is present and is a valid UUID
    assert 'UUID' in response
    assert isinstance(uuid.UUID(response['UUID']), uuid.UUID)