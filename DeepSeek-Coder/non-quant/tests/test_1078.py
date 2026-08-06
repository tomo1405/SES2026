import pytest
from src_1078 import task_func

@pytest.fixture
def example_data():
    return ["12/12/21 12:34:56.789", "12/12/21 12:34:56.789"]

def test_task_func(example_data):
    result = task_func(example_data, "UTC")
    assert result == 0.0