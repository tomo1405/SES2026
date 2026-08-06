import pytest
from src_0182 import task_func
from django.http import HttpResponse
from unittest.mock import patch

@pytest.mark.parametrize("data, min_delay, max_delay", [
    ("{'key': 'value'}", 0.1, 0.5),
    ("[1, 2, 3]", 0.2, 0.3),
    ("'string'", 0.01, 0.1)
])
@patch('time.sleep')
def test_task_func(mock_sleep, data, min_delay, max_delay):
    # Call the function
    response = task_func(data, min_delay, max_delay)

    # Check if the response is an instance of HttpResponse
    assert isinstance(response, HttpResponse)

    # Check if the content type is correct
    assert response['Content-Type'] == 'application/json'

    # Check if the content matches the input data
    assert response.content.decode('utf-8') == data

    # Check if time.sleep was called with a value between min_delay and max_delay
    mock_sleep.assert_called_once()
    sleep_arg = mock_sleep.call_args[0][0]
    assert min_delay <= sleep_arg <= max_delay