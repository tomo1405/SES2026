import pytest
from src_0512 import task_func

def test_task_func():
    # Test with valid data
    data = [
        {"Age": 25, "Salary": 50000, "Experience": 2},
        {"Age": 30, "Salary": 60000, "Experience": 4},
        {"Age": 35, "Salary": 70000, "Experience": 6},
    ]
    result, ax = task_func("Age", data)
    assert result == {
        "sum": 105,
        "mean": 35,
        "min": 25,
        "max": 35,
    }
    assert ax.get_title() == "Pie Chart of Age"
    assert ax.get_legend() == "Age"
    assert ax.get_labels() == ["25", "30", "35"]

    # Test with empty data
    data = []
    result, ax = task_func("Age", data)
    assert result == {
        "sum": 0,
        "mean": np.nan,
        "min": np.nan,
        "max": np.nan,
    }
    assert ax.get_title() == "Pie Chart of Age"
    assert ax.get_legend() == "Age"
    assert ax.get_labels() == []

    # Test with invalid column name
    with pytest.raises(ValueError):
        task_func("Invalid", data)