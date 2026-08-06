import pytest
import numpy as np
import matplotlib.pyplot as plt
from src_0911 import task_func

def test_task_func():
    letters = ['A', 'B', 'C']
    repetitions = [1, 2, 3]
    colors = ['red', 'green', 'blue']
    
    with pytest.raises(ValueError):
        task_func(letters, repetitions, [])
    
    with pytest.raises(ValueError):
        task_func([], repetitions, colors)
    
    with pytest.raises(ValueError):
        task_func(letters, [], colors)
    
    ax = task_func(letters, repetitions, colors)
    assert isinstance(ax, plt.Axes)