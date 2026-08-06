import pytest
from src_0629 import task_func

def test_task_func():
    ax = task_func()
    assert ax.get_title() == 'Random Sine Wave'
    assert ax.get_xlabel() == 'Time'
    assert ax.get_ylabel() == 'Amplitude'
    assert ax.get_grid() == True
    assert len(ax.get_lines()) == 1
    assert ax.get_lines()[0].get_color() == 'black'
    assert ax.get_lines()[0].get_linewidth() == 1
    assert ax.get_lines()[0].get_linestyle() == '-'