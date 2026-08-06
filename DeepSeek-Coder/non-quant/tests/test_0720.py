import pytest
from src_0720 import task_func

@pytest.fixture
def setup():
    return task_func

def test_task_func(setup):
    func = setup()
    assert func("test_directory", "test_word") == 0  # Replace with appropriate values

# Add more test cases as needed