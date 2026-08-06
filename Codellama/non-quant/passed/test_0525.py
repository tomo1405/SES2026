import pytest
from src_0525 import task_func

def test_task_func_empty_input():
    with pytest.raises(ValueError):
        task_func([])

def test_task_func_invalid_input():
    with pytest.raises(TypeError):
        task_func([1, 2, 3])

def test_task_func_invalid_data_type():
    with pytest.raises(TypeError):
        task_func([{"a": "b"}])

def test_task_func_valid_input():
    data = [{"a": 1, "b": 2}, {"a": 3, "b": 4}]
    result, axes = task_func(data)
    assert result == {"a": {"mean": 2, "std": 1}, "b": {"mean": 3, "std": 1}}
    assert len(axes) == 2
    assert axes[0].get_title() == "Statistics of a"
    assert axes[1].get_title() == "Statistics of b"