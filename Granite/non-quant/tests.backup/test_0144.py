import pytest
from src_0144 import task_func

def test_task_func():
    ax = task_func()
    assert ax is not None
    assert ax.get_title() == 'Solution of the equation y=2x+1 at x=2'
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'y'
    assert ax.get_xlim() == (-10, 10)
    assert ax.get_legend().get_texts()[0].get_text() == 'y=2x+1'
    assert ax.get_legend().get_texts()[1].get_text() == 'Solution at x=2'