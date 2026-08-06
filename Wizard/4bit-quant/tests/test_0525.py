python
import pytest
from src_0525 import task_func

def test_task_func_empty_input():
    with pytest.raises(ValueError):
        task_func([])

def test_task_func_invalid_input():
    with pytest.raises(TypeError):
        task_func([{"a": "b"}, {"c": "d"}])

def test_task_func_valid_input():
    data = [
        {"a": 1, "b": 2, "c": 3},
        {"a": 4, "b": 5, "c": 6},
        {"a": 7, "b": 8, "c": 9},
    ]
    result, axes = task_func(data)
    assert isinstance(result, dict)
    assert isinstance(axes, list)
    assert len(axes) == len(data)
    for ax in axes:
        assert isinstance(ax, plt.Axes)