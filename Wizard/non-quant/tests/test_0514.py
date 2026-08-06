python
import pytest
from src_0514 import task_func

def test_task_func_valid_column():
    data = [
        ["2021-01-01", 1000, 500, 20],
        ["2021-01-02", 2000, 1000, 30],
        ["2021-01-03", 1500, 750, 25],
    ]
    result, ax = task_func("Steps", data)
    assert result["sum"] == 4500
    assert result["mean"] == 1500
    assert result["min"] == 1000
    assert result["max"] == 2000
    assert ax.get_title() == "Line Chart of Steps"

def test_task_func_invalid_column():
    data = [
        ["2021-01-01", 1000, 500, 20],
        ["2021-01-02", 2000, 1000, 30],
        ["2021-01-03", 1500, 750, 25],
    ]
    with pytest.raises(KeyError):
        task_func("Heart Rate", data)

def test_task_func_empty_data():
    data = []
    with pytest.raises(ValueError):
        task_func("Steps", data)

def test_task_func_negative_values():
    data = [
        ["2021-01-01", -1000, 500, 20],
        ["2021-01-02", 2000, -1000, 30],
        ["2021-01-03", 1500, 750, -25],
    ]
    with pytest.raises(ValueError):
        task_func("Steps", data)