python
import pytest
from src_0360 import task_func

def test_task_func():
    data_dict = {'x': [1, 2, 3, 4, 5], 'y': [2, 4, 6, 8, 10]}
    data_keys = ['x', 'y']
    correlation, ax = task_func(data_dict, data_keys)
    
    assert isinstance(correlation, float)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == data_keys[0]
    assert ax.get_ylabel() == data_keys[1]
    assert ax.get_title() == f'Correlation: {correlation:.2f}'