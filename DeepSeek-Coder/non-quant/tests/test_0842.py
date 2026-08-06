import pytest
from src_0842 import task_func

@pytest.fixture
def example_input():
    return '{"text": "Hello, world! This is a test."}'

def test_task_func(example_input):
    result = task_func(example_input)
    assert isinstance(result, dict), "The result should be a dictionary."
    assert result == {'hello': 1, 'world': 1, 'this': 1, 'is': 1, 'a': 1, 'test': 1}, "The result does not match the expected output."