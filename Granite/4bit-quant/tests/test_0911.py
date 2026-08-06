import matplotlib.pyplot as plt
import pytest
from src_0911 import task_func


def test_task_func():
    letters = ['A', 'B', 'C']
    repetitions = [1, 2, 3]
    colors = ['red', 'green', 'blue']
    
    ax = task_func(letters, repetitions, colors)
    
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == 'Letters'
    assert ax.get_ylabel() == 'Frequency'
    assert ax.get_title() == 'Frequency of Letters'

def test_task_func_invalid_input():
    letters = ['A', 'B', 'C']
    repetitions = [1, 2]
    colors = ['red', 'green', 'blue']
    
    with pytest.raises(ValueError):
        task_func(letters, repetitions, colors)