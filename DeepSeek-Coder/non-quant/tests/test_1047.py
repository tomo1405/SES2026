import pytest
from src_1047 import task_func

def test_task_func():
    result = task_func("2023-04-01")
    assert len(result) == len(EMPLOYEES) * 10
    assert all(col in result.columns for col in ["Employee", "Date"])