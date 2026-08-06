import pytest
from src_1094 import task_func

@pytest.fixture
def example_input():
    return "example_input.txt"

def test_task_func(example_input):
    result = task_func(example_input)
    assert isinstance(result, list), "The result should be a list"
    assert all(isinstance(item, dict) for item in result), "All items should be dictionaries"