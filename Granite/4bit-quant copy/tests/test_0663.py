import pytest
from src_0663 import task_func

def test_task_func():
    x = [[1, 2], [3, 4]]
    y = [[5, 6], [7, 8]]
    labels = ['label1', 'label2']
    
    fig = task_func(x, y, labels)
    
    assert fig is not None
    assert fig.axes is not None
    assert len(fig.axes) == 1
    assert fig.axes[0].legend_.texts is not None
    assert len(fig.axes[0].legend_.texts) == 2
    assert fig.axes[0].legend_.texts[0].get_text() == 'label1'
    assert fig.axes[0].legend_.texts[1].get_text() == 'label2'