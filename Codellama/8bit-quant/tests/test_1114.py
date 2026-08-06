import pytest
from src_114 import task_func

def test_task_func():
    csv_file = "test_data.csv"
    emp_prefix = "EMP$$"
    expected_result = {"EMP$$1": 1, "EMP$$2": 2, "EMP$$3": 3}

    result = task_func(csv_file, emp_prefix)

    assert result == expected_result