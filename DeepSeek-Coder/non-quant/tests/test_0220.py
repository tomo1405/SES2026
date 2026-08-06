import pytest
from src_0220 import task_func

@pytest.fixture
def input_data():
    return [1, 2, 3, 4, 5]

def test_task_func(input_data):
    result = task_func(input_data)
    assert isinstance(result, tuple), "The result should be a tuple"
    assert len(result) == 6, "The result should contain 6 elements"
    assert all(isinstance(x, (int, float)) for x in result), "All elements should be numbers"