import matplotlib
import pytest
from src_0513 import task_func


def test_task_func():
    data = [
        ["Product A", 10, 100],
        ["Product B", 20, 200],
        ["Product C", 30, 300],
    ]
    column = "Quantity Sold"
    result, ax = task_func(column, data)
    assert isinstance(result, dict)
    assert "sum" in result
    assert "mean" in result
    assert "min" in result
    assert "max" in result
    assert isinstance(ax, matplotlib.axes.Axes)

def test_task_func_with_negative_values():
    data = [
        ["Product A", 10, 100],
        ["Product B", 20, 200],
        ["Product C", -30, 300],
    ]
    column = "Quantity Sold"
    with pytest.raises(ValueError):
        task_func(column, data)