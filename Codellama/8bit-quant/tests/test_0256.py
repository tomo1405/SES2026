import pytest
from src_0256 import task_func
import matplotlib.axes

def test_task_func_valid_input():
    ax = matplotlib.axes.Axes()
    func_index = 0
    result = task_func(ax, func_index)
    assert isinstance(result, matplotlib.axes.Axes)
    assert result.get_xlabel() == "x"
    assert result.get_ylabel() == "y"
    assert result.get_title() == "Function"
    assert result.get_xlim() == (0, 2 * np.pi)
    assert result.get_ylim() == (-1, 1)
    assert result.get_rlabel_position() == 0

def test_task_func_invalid_input():
    ax = "not an axes"
    func_index = 0
    with pytest.raises(ValueError):
        task_func(ax, func_index)