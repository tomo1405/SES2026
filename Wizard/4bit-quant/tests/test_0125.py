python
import pytest
from src_0125 import task_func

def test_task_func():
    with pytest.raises(TypeError):
        task_func("not a list")
    with pytest.raises(ValueError):
        task_func([1, 2, "three"])
    with pytest.raises(ValueError):
        task_func([1, 2, 3], size="not an int")
    with pytest.raises(ValueError):
        task_func([1, 2, 3], seed="not an int")

    start_time, ax = task_func([1, 2, 3], size=100, seed=100)
    assert isinstance(start_time, float)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Histogram of Random Numbers'
    assert ax.get_xlabel() == 'Number'
    assert ax.get_ylabel() == 'Frequency'