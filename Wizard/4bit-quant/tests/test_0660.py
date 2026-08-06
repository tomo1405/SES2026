python
import pytest
from src_0660 import task_func

def test_task_func():
    x = [np.arange(0, 1, 0.1), np.arange(0, 1, 0.1)]
    y = [np.random.normal(0, 1, 100), np.random.normal(0, 1, 100)]
    labels = ['A', 'B']
    
    fig = task_func(x, y, labels)
    
    assert isinstance(fig, plt.Figure)