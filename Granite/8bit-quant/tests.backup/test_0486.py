import pytest
from src_0486 import task_func

def test_task_func():
    ax = task_func("2023-01-01", "2023-01-08")
    assert ax is not None
    assert ax.get_xlabel() == "Date"
    assert ax.get_ylabel() == "Time difference (hours)"
    legend_labels = [line.get_label() for line in ax.get_lines()]
    assert legend_labels == ["UTC", "America/Los_Angeles", "Europe/Paris", "Asia/Kolkata", "Australia/Sydney"]