import pytest
from src_0512 import task_func

def test_task_func():
    # Test with valid data
    data = {"Age": [20, 30, 40], "Salary": [50000, 60000, 70000], "Experience": [5, 10, 15]}
    column = "Age"
    result, ax = task_func(column, data)
    assert result == {"sum": 90, "mean": 30, "min": 20, "max": 40}
    assert ax.get_title() == "Pie Chart of Age"
    assert ax.get_legend() == ["20", "30", "40"]

    # Test with empty data
    data = {}
    column = "Age"
    result, ax = task_func(column, data)
    assert result == {"sum": 0, "mean": np.nan, "min": np.nan, "max": np.nan}
    assert ax.get_title() == "Pie Chart of Age"
    assert ax.get_legend() == []

    # Test with invalid data
    data = {"Age": [20, 30, 40], "Salary": [50000, 60000, 70000], "Experience": [5, 10, 15]}
    column = "Invalid"
    with pytest.raises(KeyError):
        task_func(column, data)