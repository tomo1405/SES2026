import pytest
from src_1049 import task_func

def test_task_func():
    ax = task_func("2023-03-14")
    assert ax is not None
    assert ax.get_title() == "Sine Wave for 2023-03-14 (Frequency: 14)"