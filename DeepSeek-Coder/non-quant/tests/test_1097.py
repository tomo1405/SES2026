import pytest
from src_1097 import task_func

@pytest.fixture
def sample_data():
    return "This is a test text with $dollar and $words."

def test_task_func(sample_data):
    filename = "test_output.csv"
    result = task_func(sample_data, filename)
    assert os.path.exists(result)
    os.remove(filename)