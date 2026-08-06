import pytest
from src_0256 import task_func
import matplotlib.axes

def test_task_func_valid_input():
    ax = matplotlib.axes.Axes()
    func_index = 0
    result = task_func(ax, func_index)
    assert isinstance(result, matplotlib.axes.Axes)
    assert result.get_rlabel_position() == 0

def test_task_func_invalid_input():
    ax = "not an axes"
    func_index = 0
    with pytest.raises(ValueError):
        task_func(ax, func_index)