import pytest
from src_0669 import task_func

def test_task_func():
    assert task_func("ABCD") == ["A", "B", "C", "D"]
    assert task_func("ABABC") == ["A", "B", "A", "B"]
    assert task_func("ABCDABC") == ["A", "B", "C", "D"]
    assert task_func("ABCDEF") == ["A", "B", "C", "D", "E", "F"]

def test_task_func_empty_string():
    with pytest.raises(ValueError):
        task_func("")

def test_task_func_invalid_input():
    with pytest.raises(TypeError):
        task_func(123)