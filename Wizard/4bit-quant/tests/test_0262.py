python
import pytest
from src_0262 import task_func

def test_task_func():
    fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))
    radius = 1.5
    with pytest.raises(ValueError):
        task_func(ax, -radius)
    with pytest.raises(TypeError):
        task_func(plt.subplot(111), radius)
    task_func(ax, radius)
    assert ax.get_rlabel_position() == radius * 45
    plt.close()