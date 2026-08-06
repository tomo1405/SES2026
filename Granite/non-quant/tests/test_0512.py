import pytest
from src_0512 import task_func

def test_task_func():
    data = [
        ["Age", "Salary", "Experience"],
        [25, 50000, 3],
        [30, 60000, 5],
        [35, 70000, 7],
        [40, 80000, 10]
    ]
    column = "Salary"
    expected_result = {
        "sum": 300000,
        "mean": 60000.0,
        "min": 50000.0,
        "max": 80000.0
    }
    expected_ax_title = "Pie Chart of Salary"

    result, ax = task_func(column, data)

    assert result == expected_result
    assert ax.get_title() == expected_ax_title