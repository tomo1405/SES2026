import time

from src_0182 import task_func


def test_task_func():
    # Test that the function returns a HttpResponse object
    response = task_func('{"name": "John Doe"}', 0, 1)
    assert isinstance(response, HttpResponse)

    # Test that the response has the correct content type
    assert response['Content-Type'] == 'application/json'

    # Test that the response has the correct data
    assert response.content == b'{"name": "John Doe"}'

def test_task_func_delay():
    # Test that the function waits for the correct amount of time
    start_time = time.time()
    task_func('{"name": "John Doe"}', 1, 2)
    end_time = time.time()
    assert end_time - start_time >= 1

    # Test that the function waits for the correct amount of time
    start_time = time.time()
    task_func('{"name": "John Doe"}', 2, 3)
    end_time = time.time()
    assert end_time - start_time >= 2