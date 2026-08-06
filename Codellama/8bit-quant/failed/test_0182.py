import pytest
from src_0182 import task_func

def test_task_func():
    data = {'key': 'value'}
    min_delay = 1
    max_delay = 5

    # Test that the function returns a HttpResponse object
    response = task_func(data, min_delay, max_delay)
    assert isinstance(response, HttpResponse)

    # Test that the response has the correct content type
    assert response['Content-Type'] == 'application/json'

    # Test that the response has the correct data
    assert response.content == b'{"key": "value"}'

def test_task_func_with_invalid_data():
    data = {'key': 'value'}
    min_delay = 1
    max_delay = 5

    # Test that the function raises a ValueError if the data is not a dictionary
    with pytest.raises(ValueError):
        task_func(1, min_delay, max_delay)

    # Test that the function raises a ValueError if the min_delay is not a number
    with pytest.raises(ValueError):
        task_func(data, 'a', max_delay)

    # Test that the function raises a ValueError if the max_delay is not a number
    with pytest.raises(ValueError):
        task_func(data, min_delay, 'a')

def test_task_func_with_invalid_delay():
    data = {'key': 'value'}
    min_delay = 1
    max_delay = 5

    # Test that the function raises a ValueError if the min_delay is greater than the max_delay
    with pytest.raises(ValueError):
        task_func(data, max_delay, min_delay)

    # Test that the function raises a ValueError if the min_delay is negative
    with pytest.raises(ValueError):
        task_func(data, -1, max_delay)

    # Test that the function raises a ValueError if the max_delay is negative
    with pytest.raises(ValueError):
        task_func(data, min_delay, -1)