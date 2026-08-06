import pytest
from src_0182 import task_func
from django.http import HttpResponse
from django.conf import settings
import random
import time

def test_task_func():
    data = "example data"
    min_delay = 0.1
    max_delay = 0.5

    # Generate a random delay
    delay = random.uniform(min_delay, max_delay)

    # Wait for the delay
    time.sleep(delay)

    response = task_func(data, min_delay, max_delay)

    assert isinstance(response, HttpResponse)
    assert response.content_type == 'application/json'
    assert response.content.decode('utf-8') == data