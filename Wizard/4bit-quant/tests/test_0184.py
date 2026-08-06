python
import uuid
import pytest
from django.http import HttpResponse

def task_func(data):

    response = HttpResponse(data, content_type='application/json')

    # Generate a UUID
    request_uuid = uuid.uuid4()

    # Add the UUID to the response headers
    response['UUID'] = str(request_uuid)

    return response

def test_task_func():
    # Test with valid data
    data = '{"key": "value"}'
    response = task_func(data)
    assert response.content == b'{"key": "value"}'
    assert response['UUID'] == str(uuid.uuid4())

    # Test with invalid data
    data = 'invalid data'
    with pytest.raises(TypeError):
        task_func(data)