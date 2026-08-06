import pytest
from src_0848 import task_func

@pytest.fixture
def setup():
    return task_func("input_string", "./text_files")

def test_task_func(setup):
    assert isinstance(setup, list)
    assert all(isinstance(path, str) for path in setup)
    assert all(os.path.isfile(path) for path in setup)