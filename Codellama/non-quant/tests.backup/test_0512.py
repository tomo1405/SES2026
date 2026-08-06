import pytest
from src_0512 import task_func

def test_task_func():
    # Test with valid data
    data = [
        {"Age": 25, "Salary": 50000, "Experience": 2},
        {"Age": 30, "Salary": 60000, "Experience": 4},
        {"Age": 35, "Salary": 70000, "Experience": 6},
    ]
    column = "Salary"
    result, ax = task_func(column, data)
    assert result["sum"] == 180000
    assert result["mean"] == 60000
    assert result["min"] == 50000
    assert result["max"] == 70000
    assert ax.get_title() == "Pie Chart of Salary"

    # Test with empty data
    data = []
    column = "Salary"
    result, ax = task_func(column, data)
    assert result["sum"] == 0
    assert result["mean"] == np.nan
    assert result["min"] == np.nan
    assert result["max"] == np.nan
    assert ax.get_title() == "Pie Chart of Salary"

    # Test with invalid column
    data = [
        {"Age": 25, "Salary": 50000, "Experience": 2},
        {"Age": 30, "Salary": 60000, "Experience": 4},
        {"Age": 35, "Salary": 70000, "Experience": 6},
    ]
    column = "Invalid"
    with pytest.raises(KeyError):
        task_func(column, data)