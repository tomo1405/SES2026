import pytest
from src_0512 import task_func

def test_task_func():
    column = "Age"
    data = [
        {"Age": 25, "Salary": 50000, "Experience": 3},
        {"Age": 30, "Salary": 60000, "Experience": 5},
        {"Age": 35, "Salary": 70000, "Experience": 8},
    ]

    result, ax = task_func(column, data)

    assert result["sum"] == 90
    assert result["mean"] == 30
    assert result["min"] == 25
    assert result["max"] == 35

    assert ax.get_title() == "Pie Chart of Age"

if __name__ == "__main__":
    pytest.main()