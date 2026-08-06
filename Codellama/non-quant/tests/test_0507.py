import pytest
from src_0507 import task_func

def test_task_func():
    # Test with valid input
    column = "Temperature"
    data = [
        ["2022-01-01", 20, 60, 3, 0],
        ["2022-01-02", 22, 55, 4, 0],
        ["2022-01-03", 18, 70, 2, 0],
        ["2022-01-04", 24, 50, 5, 0],
        ["2022-01-05", 21, 65, 3, 0],
    ]
    result = task_func(column, data)
    assert result["sum"] == 120
    assert result["mean"] == 21
    assert result["min"] == 3
    assert result["max"] == 24
    assert isinstance(result["plot"], matplotlib.axes.Axes)

    # Test with invalid input
    with pytest.raises(ValueError):
        task_func("Invalid column", data)

    with pytest.raises(ValueError):
        task_func(column, [])