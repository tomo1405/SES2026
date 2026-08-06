import pytest
from src_0267 import task_func

@pytest.fixture
def setup():
    return "test_path"

def test_task_func(setup):
    result = task_func(setup)
    assert result == os.path.join(setup, 'file_sizes.csv')