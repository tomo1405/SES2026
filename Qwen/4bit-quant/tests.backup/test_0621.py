import pytest
from src_0621 import task_func

def test_task_func_input_type():
    with pytest.raises(TypeError):
        task_func("not a list")

def test_task_func_input_length():
    with pytest.raises(IndexError):
        task_func([[1, 2]])

def test_task_func_input_values():
    with pytest.raises(ValueError):
        task_func([[1, 2], [3, "a"]])

def test_task_func_output_shape():
    result = task_func([[2, 3], [4, 5]])
    assert result.shape == (6, 15)

def test_task_func_output_range():
    result = task_func([[2, 3], [4, 5]])
    assert result.values.min() >= 1 and result.values.max() <= 100

def test_task_func_randomness():
    result1 = task_func([[2, 3], [4, 5]])
    result2 = task_func([[2, 3], [4, 5]])
    assert not result1.equals(result2)