import pytest
from django.http import HttpResponse
from src_0184 import task_func

def test_task_func():
    # Test data
    data = '{"key": "value"}'

    # Call the function
    response = task_func(data)

    # Check if the response is an instance of HttpResponse
    assert isinstance(response, HttpResponse)

    # Check if the content type is correct
    assert response['Content-Type'] == 'application/json'

    # Check if the response content matches the input data
    assert response.content.decode('utf-8') == data

    # Check if the UUID header is present and is a valid UUID string
    assert 'UUID' in response
    assert len(response['UUID']) == 36  # UUID length in string format

    # Try to convert the UUID string to a UUID object to ensure it's valid
    try:
        uuid.UUID(response['UUID'])
    except ValueError:
        pytest.fail("The UUID in the response header is not a valid UUID")

# Run the tests
if __name__ == "__main__":
    pytest.main()