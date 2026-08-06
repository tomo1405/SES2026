import pytest
from src_0512 import task_func

def test_task_func():
    column = "Age"
    data = [
        ["John", 25, 50000, 2],
        ["Jane", 30, 60000, 3],
        ["Bob", 35, 70000, 4],
    ]

    result, ax = task_func(column, data)

    assert result["sum"] == 135
    assert result["mean"] == 45
    assert result["min"] == 25
    assert result["max"] == 50000

    assert ax.get_title() == "Pie Chart of Age"

if __name__ == "__main__":
    pytest.main()