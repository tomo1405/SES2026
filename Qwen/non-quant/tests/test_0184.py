import pytest
from src_0184 import task_func
from django.http import HttpResponse
import uuid

def test_task_func():
    # Test data
    test_data = '{"key": "value"}'
    
    # Expected response
    expected_response = HttpResponse(test_data, content_type='application/json')
    
    # Call the function
    actual_response = task_func(test_data)
    
    # Check if the response is an instance of HttpResponse
    assert isinstance(actual_response, HttpResponse)
    
    # Check if the content is correct
    assert actual_response.content.decode('utf-8') == test_data
    
    # Check if the content type is correct
    assert actual_response['Content-Type'] == 'application/json'
    
    # Check if the UUID header is present and is a valid UUID
    assert 'UUID' in actual_response
    try:
        uuid.UUID(actual_response['UUID'])
    except ValueError:
        pytest.fail("UUID header is not a valid UUID")