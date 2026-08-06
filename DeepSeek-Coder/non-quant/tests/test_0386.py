import pytest
from src_0386 import task_func
from collections import Counter
import matplotlib.pyplot as plt

def test_task_func():
    fruit_dict = {
        'fruit1': 'Apple',
        'fruit2': 'Banana',
        'fruit3': 'Cherry',
        'fruit4': 'Date',
        'fruit5': 'Elderberry'
    }
    
    result = task_func(fruit_dict=fruit_dict)
    
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], Counter)
    assert isinstance(result[1], plt.Axes)

    # Additional assertions to check the plot
    plt.close()