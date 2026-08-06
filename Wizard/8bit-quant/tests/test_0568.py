python
import pytest
from src_0568 import task_func

def test_task_func():
    data = '1-2-3-4-5-6-7-8-9-10'
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)