import pytest
from src_0514 import task_func

def test_task_func_valid_column():
    data = [
        ["2022-01-01", 1000, 200, 3],
        ["2022-01-02", 1200, 250, 4],
        ["2022-01-03", 1400, 300, 5],
    ]
    result, ax = task_func("Steps", data)
    assert result["sum"] == 3600
    assert result["mean"] == 1200
    assert result["min"] == 1000
    assert result["max"] == 1400
    assert ax.get_ylabel() == "Steps"
    assert ax.get_title() == "Line Chart of Steps"

def test_task_func_invalid_column():
    data = [
        ["2022-01-01", 1000, 200, 3],
        ["2022-01-02", 1200, 250, 4],
        ["2022-01-03", 1400, 300, 5],
    ]
    with pytest.raises(KeyError):
        task_func("Invalid Column", data)

def test_task_func_no_data():
    with pytest.raises(ValueError):
        task_func("Steps", [])

def test_task_func_negative_values():
    data = [
        ["2022-01-01", -1000, 200, 3],
        ["2022-01-02", 1200, -250, 4],
        ["2022-01-03", 1400, 300, -5],
    ]
    with pytest.raises(ValueError):
        task_func("Steps", data)