python
import pytest
from src_0497 import task_func

def test_task_func():
    with pytest.raises(ValueError):
        task_func(days_in_past=0)

    with pytest.raises(ValueError):
        task_func(days_in_past=-1)

    ax = task_func(days_in_past=7)
    assert isinstance(ax, plt.Axes)