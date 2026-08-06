import pytest
from src_0722 import task_func

@pytest.fixture
def sample_data():
    return "sample.csv"

def test_task_func(sample_data):
    result = task_func(sample_data)
    assert result is not None
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], str)
    assert isinstance(result[1], int)