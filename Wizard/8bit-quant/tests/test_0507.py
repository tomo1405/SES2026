python
import pytest
from src_0507 import task_func

def test_task_func():
    data = [
        ["2022-01-01", 25, 60, 10, 0],
        ["2022-01-02", 20, 70, 20, 10],
        ["2022-01-03", 22, 65, 15, 5],
        ["2022-01-04", 28, 55, 5, 20],
        ["2022-01-05", 23, 68, 12, 15],
    ]
    column = "Temperature"
    result = task_func(column, data)
    assert result["sum"] == 170
    assert result["mean"] == 22.0
    assert result["min"] == 20
    assert result["max"] == 28
    assert isinstance(result["plot"], plt.Axes)