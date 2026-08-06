python
import pytest
from src_0471 import task_func

def test_task_func():
    myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ax = task_func(myList)
    assert ax.get_xlabel() == "Value"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Histogram of Values"