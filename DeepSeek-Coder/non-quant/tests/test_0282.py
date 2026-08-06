import pytest
from src_0282 import task_func

@pytest.fixture
def example_data():
    return "example_data"

def test_task_func(example_data):
    result = task_func("example_data")
    assert isinstance(result, dict), "The result should be a dictionary."
    assert len(result) > 0, "The result dictionary should not be empty."