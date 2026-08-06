python
import pytest
from src_0182 import task_func

@pytest.mark.parametrize("data, min_delay, max_delay, expected_response", [
    ('{"message": "Hello, world!"}', 0, 0, '{"message": "Hello, world!"}'),
    ('{"message": "Hello, world!"}', 1, 1, '{"message": "Hello, world!"}'),
    ('{"message": "Hello, world!"}', 2, 2, '{"message": "Hello, world!"}'),
    ('{"message": "Hello, world!"}', 3, 3, '{"message": "Hello, world!"}'),
    ('{"message": "Hello, world!"}', 4, 4, '{"message": "Hello, world!"}'),
    ('{"message": "Hello, world!"}', 5, 5, '{"message": "Hello, world!"}'),
    ('{"message": "Hello, world!"}', 6, 6, '{"message": "Hello, world!"}'),
    ('{"message": "Hello, world!"}', 7, 7, '{"message": "Hello, world!"}'),
    ('{"message": "Hello, world!"}', 8, 8, '{"message": "Hello, world!"}'),
    ('{"message": "Hello, world!"}', 9, 9, '{"message": "Hello, world!"}'),
    ('{"message": "Hello, world!"}', 10, 10, '{"message": "Hello, world!"}'),
])
def test_task_func(data, min_delay, max_delay, expected_response):
    response = task_func(data, min_delay, max_delay)
    assert response.content.decode('utf-8') == expected_response