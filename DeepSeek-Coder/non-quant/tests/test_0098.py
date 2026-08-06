import pytest
from src_0098 import task_func

@pytest.fixture
def example_data():
    return [1, 2, 3, 4]

def test_task_func(example_data):
    result = task_func(example_data)
    assert result == 13.794