import pytest
from src_0182 import task_func

def test_task_func():
    # Test case 1: Test that the function returns a HttpResponse object
    data = {'key': 'value'}
    min_delay = 0.1
    max_delay = 0.5
    response = task_func(data, min_delay, max_delay)
    assert isinstance(response, HttpResponse)

    # Test case 2: Test that the function returns a response with the correct data
    data = {'key': 'value'}
    min_delay = 0.1
    max_delay = 0.5
    response = task_func(data, min_delay, max_delay)
    assert response.content == b'{"key": "value"}'

    # Test case 3: Test that the function returns a response with the correct content type
    data = {'key': 'value'}
    min_delay = 0.1
    max_delay = 0.5
    response = task_func(data, min_delay, max_delay)
    assert response['Content-Type'] == 'application/json'

    # Test case 4: Test that the function raises an error if the data is not a dictionary
    data = 'not a dictionary'
    min_delay = 0.1
    max_delay = 0.5
    with pytest.raises(TypeError):
        task_func(data, min_delay, max_delay)

    # Test case 5: Test that the function raises an error if the min_delay is not a number
    data = {'key': 'value'}
    min_delay = 'not a number'
    max_delay = 0.5
    with pytest.raises(TypeError):
        task_func(data, min_delay, max_delay)

    # Test case 6: Test that the function raises an error if the max_delay is not a number
    data = {'key': 'value'}
    min_delay = 0.1
    max_delay = 'not a number'
    with pytest.raises(TypeError):
        task_func(data, min_delay, max_delay)

    # Test case 7: Test that the function raises an error if the min_delay is greater than the max_delay
    data = {'key': 'value'}
    min_delay = 0.5
    max_delay = 0.1
    with pytest.raises(ValueError):
        task_func(data, min_delay, max_delay)