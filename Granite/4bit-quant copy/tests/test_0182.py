import pytest
from django.http import HttpResponse
from django.conf import settings
import random
import time
def task_func(data, min_delay, max_delay):

    # Generate a random delay
    delay = random.uniform(min_delay, max_delay)

    # Wait for the delay
    time.sleep(delay)

    response = HttpResponse(data, content_type='application/json')

    return response

def test_task_func():
    data = '{"key": "value"}'
    min_delay = 0.1
    max_delay = 0.5
    response = task_func(data, min_delay, max_delay)
    assert response.content_type == 'application/json'
    assert response.content == b'{"key": "value"}'

def test_task_func_invalid_data():
    data = 'invalid data'
    min_delay = 0.1
    max_delay = 0.5
    with pytest.raises(ValueError):
        task_func(data, min_delay, max_delay)

def test_task_func_invalid_delay():
    data = '{"key": "value"}'
    min_delay = -0.1
    max_delay = 0.5
    with pytest.raises(ValueError):
        task_func(data, min_delay, max_delay)

def test_task_func_invalid_max_delay():
    data = '{"key": "value"}'
    min_delay = 0.1
    max_delay = -0.5
    with pytest.raises(ValueError):
        task_func(data, min_delay, max_delay)