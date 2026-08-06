import pytest
from src_0507 import task_func

def test_task_func():
    # Test with valid input
    column = "Temperature"
    data = [
        ["2022-01-01", 20, 50, 10, 0],
        ["2022-01-02", 25, 60, 15, 0],
        ["2022-01-03", 30, 70, 20, 0],
    ]
    result = task_func(column, data)
    assert result["sum"] == 85
    assert result["mean"] == 28.333333333333332
    assert result["min"] == 10
    assert result["max"] == 30
    assert isinstance(result["plot"], matplotlib.axes.Axes)

    # Test with invalid input
    with pytest.raises(ValueError):
        task_func("Invalid column", data)

    with pytest.raises(ValueError):
        task_func(column, [])