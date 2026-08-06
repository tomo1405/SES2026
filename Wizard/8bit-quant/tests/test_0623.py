python
import pytest
from src_0623 import task_func

def test_task_func():
    L = [[1, 2, 3], [4, 5, 6]]
    ax = task_func(L)
    assert ax.get_title() == "Fit results: mu = 3.50,  std = 1.70"