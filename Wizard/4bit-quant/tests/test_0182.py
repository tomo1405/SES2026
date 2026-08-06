python
import pytest
from src_0182 import task_func

@pytest.mark.parametrize("data, min_delay, max_delay, expected_response", [
    ('{"message": "Hello, world!"}', 0, 0, b'{"message": "Hello, world!"}'),
    ('{"message": "Hello, world!"}', 1, 1, b'{"message": "Hello, world!"}'),
    ('{"message": "Hello, world!"}', 2, 2, b'{"message": "Hello, world!"}'),
    ('{"message": "Hello, world!"}', 3, 3, b'{"message": "Hello, world!"}'),
    ('{"message": "Hello, world!"}', 4, 4, b'{"message": "Hello, world!"}'),
    ('{"message": "Hello, world!"}', 5, 5, b'{"message": "Hello, world!"}'),
    ('{"message": "Hello, world!"}', 6, 6, b'{"message": "Hello, world!"}'),
    ('{"message": "Hello, world!"}', 7, 7, b'{"message": "Hello, world!"}'),
    ('{"message": "Hello, world!"}', 8, 8, b'{"message": "Hello, world!"}'),
    ('{"message": "Hello, world!"}', 9, 9, b'{"message": "Hello, world!"}'),
    ('{"message": "Hello, world!"}', 10, 10, b'{"message": "Hello, world!"}'),
])
def test_task_func(data, min_delay, max_delay, expected_response):
    response = task_func(data, min_delay, max_delay)
    assert response.content == expected_response