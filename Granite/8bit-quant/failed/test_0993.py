import pytest
from src_0993 import task_func

def test_task_func():
    assert task_func() == "path/to/whatever"
    assert task_func("new_path") == "new_path"

def test_task_func_with_database():
    assert task_func(database="new_database.db") == "path/to/whatever"
    assert task_func(path_to_append="new_path", database="new_database.db") == "new_path"

def test_task_func_with_invalid_parameters():
    with pytest.raises(TypeError):
        task_func(123)
    with pytest.raises(TypeError):
        task_func(path_to_append=123)
    with pytest.raises(TypeError):
        task_func(database=123)