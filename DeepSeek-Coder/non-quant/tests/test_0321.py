import pytest
from src_0321 import task_func

@pytest.fixture
def setup():
    return "test_directory", ["file1", "file2"]

def test_task_func(setup):
    directory, file_list = setup
    result = task_func(directory, file_list)
    assert result is not None

def test_task_func_empty_list(setup):
    directory, file_list = setup
    result = task_func(directory, [])
    assert result is None

def test_task_func_exception(setup):
    directory, file_list = setup
    with pytest.raises(Exception):
        task_func(directory, file_list)