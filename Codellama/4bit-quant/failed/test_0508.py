import pytest
from src_0508 import task_func

def test_task_func():
    # Test with valid column and data
    column = "Open"
    data = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
    ]
    result = task_func(column, data)
    assert result == {
        "sum": 35,
        "mean": 17.5,
        "min": 1,
        "max": 10,
    }

    # Test with invalid column
    column = "Invalid"
    data = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
    ]
    with pytest.raises(ValueError):
        task_func(column, data)

    # Test with invalid data
    column = "Open"
    data = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9],
    ]
    with pytest.raises(ValueError):
        task_func(column, data)