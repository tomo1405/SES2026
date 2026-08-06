import pytest
from src_0629 import task_func

def test_task_func():
    ax = task_func()
    assert ax.get_title() == 'Random Sine Wave'
    assert ax.get_xlabel() == 'Time'
    assert ax.get_ylabel() == 'Amplitude'
    assert ax.get_grid() == True
    assert len(ax.get_lines()) == 1
    assert ax.get_lines()[0].get_label() == 'Random Sine Wave'
    assert ax.get_lines()[0].get_xdata() == [i/100 for i in range(1000)]
    assert ax.get_lines()[0].get_ydata() == [amplitude * math.sin(2 * math.pi * frequency * (xi + phase_shift)) for xi in x]