import pytest
from src_0378 import task_func

def test_task_func():
    result = task_func()
    assert isinstance(result, str), "The function should return a string representation of the table."
    assert "CPU Usage (%)".lower() in result.lower(), "The table should display CPU usage."
    assert "Memory Usage (%)".lower() in result.lower(), "The table should display memory usage."
    assert "Disk Usage (%)".lower() in result.lower(), "The table should display disk usage."