import pytest
from src_0508 import task_func


def test_task_func_valid_column():
    column = "Close"
    data = [
        ["2022-01-01", 100, 110, 90, 105, 1000],
        ["2022-01-02", 105, 115, 95, 110, 1100],
        ["2022-01-03", 110, 120, 100, 115, 1200],
    ]
    expected_result = {
        "sum": 340,
        "mean": 113.33333333333333,
        "min": 90,
        "max": 120,
    }
    result = task_func(column, data)
    assert result == expected_result

def test_task_func_invalid_column():
    column = "Invalid"
    data = [
        ["2022-01-01", 100, 110, 90, 105, 1000],
        ["2022-01-02", 105, 115, 95, 110, 1100],
        ["2022-01-03", 110, 120, 100, 115, 1200],
    ]
    with pytest.raises(ValueError) as exc_info:
        task_func(column, data)
    assert str(exc_info.value) == "Invalid column name."

def test_task_func_invalid_data():
    column = "Close"
    data = [
        ["2022-01-01", 100, 110, 90, 105, 1000],
        ["2022-01-02", 105, 115, 95, 110, 1100],
        ["2022-01-03", 110, 120, 100, 115, 1200],
        ["2022-01-04", 115, 125, 105, 120, 1300],
        ["2022-01-05", 120, 130, 110, 125, 1400],
    ]
    with pytest.raises(ValueError) as exc_info:
        task_func(column, data)
    assert str(exc_info.value) == "Data must be a list of lists, with each inner list matching the length of the column names."