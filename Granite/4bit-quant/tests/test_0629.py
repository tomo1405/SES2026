import pytest
from src_0629 import task_func

def test_task_func():
    ax = task_func()
    assert ax is not None, "The function should return an axis object"
    assert ax.get_title() == 'Random Sine Wave', "The title of the plot should be 'Random Sine Wave'"
    assert ax.get_xlabel() == 'Time', "The x-label of the plot should be 'Time'"
    assert ax.get_ylabel() == 'Amplitude', "The y-label of the plot should be 'Amplitude'"
    assert ax.get_gridspec() is not None, "The plot should have a grid"