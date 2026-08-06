import pytest
from src_0537 import task_func
import os

@pytest.fixture
def setup_and_teardown():
    # Setup code here
    yield
    # Teardown code here

def test_task_func(setup_and_teardown):
    # Test cases
    result = task_func("test_db", "test_table")
    assert os.path.exists(result)
    os.remove(result)  # Clean up the generated CSV file