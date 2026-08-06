python
import pytest
from src_0400 import task_func

def test_task_func():
    with pytest.raises(ValueError):
        task_func(-1)
    with pytest.raises(ValueError):
        task_func(0)
    with pytest.raises(ValueError):
        task_func(1, -1)
    with pytest.raises(ValueError):
        task_func(1, 0)

    fig, ax = task_func(1, 100)
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)