import pytest
from src_0663 import task_func

def test_task_func():
    x = [[1, 2], [3, 4], [5, 6]]
    y = [[7, 8], [9, 10], [11, 12]]
    labels = ['label1', 'label2', 'label3']
    
    fig = task_func(x, y, labels)
    
    assert fig is not None
    assert fig.axes is not None
    assert len(fig.axes) == 1
    assert fig.axes[0].legend_.texts is not None
    assert len(fig.axes[0].legend_.texts) == 3
    assert all(text.get_text() in labels for text in fig.axes[0].legend_.texts)