import pytest
from src_0508 import task_func


def test_task_func_valid_column():
    column = "Open"
    data = [
        ["2022-01-01", 100, 110, 90, 105, 1000],
        ["2022-01-02", 110, 120, 100, 115, 1100],
        ["2022-01-03", 105, 115, 100, 110, 1050],
    ]
    expected_result = {
        "sum": 340,
        "mean": 113.33333333333333,
        "min": 100,
        "max": 120,
    }
    result = task_func(column, data)
    assert result == expected_result

def test_task_func_invalid_column():
    column = "Invalid"
    data = [
        ["2022-01-01", 100, 110, 90, 105, 1000],
        ["2022-01-02", 110, 120, 100, 115, 1100],
        ["2022-01-03", 105, 115, 100, 110, 1050],
    ]
    with pytest.raises(ValueError, match="Invalid column name."):
        task_func(column, data)

def test_task_func_invalid_data():
    column = "Open"
    data = [
        ["2022-01-01", 100, 110, 90, 105, 1000],
        ["2022-01-02", 110, 120, 100, 115, 1100],
        ["2022-01-03", 105, 115, 100, 110, 1050],
        ["2022-01-04", 100, 110, 90, 105, "Invalid"],
    ]
    with pytest.raises(ValueError, match="Data must be a list of lists, with each inner list matching the length of the column names."):
        task_func(column, data)