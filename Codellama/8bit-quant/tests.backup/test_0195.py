import pytest
from src_0195 import task_func

def test_task_func():
    data, color = task_func(10)
    assert isinstance(data, np.ndarray)
    assert data.shape == (10,)
    assert isinstance(color, str)
    assert color in BAR_COLOR
    assert plt.hist(data, bins=np.arange(-3, 4, 0.5), color=color, edgecolor='black')