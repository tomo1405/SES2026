import pytest
from src_0182 import task_func
from django.http import HttpResponse
from unittest.mock import patch

@pytest.mark.parametrize("data, min_delay, max_delay", [
    ("{}", 0.1, 0.5),
    ('{"key": "value"}', 0.2, 0.3),
    ('[1, 2, 3]', 0.1, 0.4)
])
@patch('time.sleep')
def test_task_func(mock_sleep, data, min_delay, max_delay):
    response = task_func(data, min_delay, max_delay)
    
    # Assert that time.sleep was called with a value between min_delay and max_delay
    mock_sleep.assert_called_once_with(pytest.approx(random.uniform(min_delay, max_delay), abs=0.01))
    
    # Assert that the response is an instance of HttpResponse
    assert isinstance(response, HttpResponse)
    
    # Assert that the response content is equal to the input data
    assert response.content.decode() == data
    
    # Assert that the response content type is 'application/json'
    assert response['Content-Type'] == 'application/json'