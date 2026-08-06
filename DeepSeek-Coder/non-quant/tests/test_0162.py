import pytest
from src_0162 import task_func
import os

@pytest.fixture
def test_data():
    return 'test_log.txt'

def test_task_func(test_data):
    result = task_func(test_data)
    assert os.path.exists(result)
    os.remove(result)  # Clean up