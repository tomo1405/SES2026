import pytest
from src_1049 import task_func

def test_task_func():
    ax = task_func("2023-01-01")
    assert ax is not None
    assert ax.get_title() == "Sine Wave for 2023-01-01 (Frequency: 1)"