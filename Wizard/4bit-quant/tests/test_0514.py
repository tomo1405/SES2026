python
import pytest
from src_0514 import task_func

def test_task_func_valid_column():
    data = [
        ["2021-01-01", 1000, 500, 20],
        ["2021-01-02", 2000, 1000, 30],
        ["2021-01-03", 3000, 1500, 40],
    ]
    result, ax = task_func("Steps", data)
    assert result["sum"] == 6000
    assert result["mean"] == 2000
    assert result["min"] == 1000
    assert result["max"] == 3000
    assert ax.get_title() == "Line Chart of Steps"

def test_task_func_invalid_column():
    data = [
        ["2021-01-01", 1000, 500, 20],
        ["2021-01-02", 2000, 1000, 30],
        ["2021-01-03", 3000, 1500, 40],
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
        ["2021-01-03", 3000, 1500, -40],
    ]
    with pytest.raises(ValueError):
        task_func("Steps", data)