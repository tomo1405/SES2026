import pytest
from src_1051 import task_func

@pytest.fixture
def input_string():
    return """Line one
Line two
Third line
"""

def test_task_func(input_string):
    result = task_func(input_string)
    assert len(result) == 3  # Assuming each line results in a file
    assert all(os.path.exists(path) for path in result)