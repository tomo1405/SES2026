import pytest
from src_0508 import task_func

def test_task_func_valid_column():
    data = [
        ["2022-01-01", 10, 20, 30, 40, 50],
        ["2022-01-02", 10, 20, 30, 40, 50],
        ["2022-01-03", 10, 20, 30, 40, 50],
    ]
    result = task_func("Open", data)
    assert result["sum"] == 30
    assert result["mean"] == 10
    assert result["min"] == 10
    assert result["max"] == 20

def test_task_func_invalid_column():
    data = [
        ["2022-01-01", 10, 20, 30, 40, 50],
        ["2022-01-02", 10, 20, 30, 40, 50],
        ["2022-01-03", 10, 20, 30, 40, 50],
    ]
    with pytest.raises(ValueError):
        task_func("Invalid", data)

def test_task_func_invalid_data():
    data = [
        ["2022-01-01", 10, 20, 30, 40, 50],
        ["2022-01-02", 10, 20, 30, 40, 50],
        ["2022-01-03", 10, 20, 30, 40, 50],
    ]
    with pytest.raises(ValueError):
        task_func("Open", data[0])

def test_task_func_empty_data():
    data = []
    result = task_func("Open", data)
    assert result["sum"] == 0
    assert result["mean"] == 0
    assert result["min"] == 0
    assert result["max"] == 0