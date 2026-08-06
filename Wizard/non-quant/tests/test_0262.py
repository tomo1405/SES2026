python
import pytest
from src_0262 import task_func

def test_task_func():
    fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))
    radius = 1
    task_func(ax, radius)
    assert ax.get_rlabel_position() == radius * 45
    assert ax.lines[0].get_ydata()[0] == radius
    plt.close()

def test_task_func_negative_radius():
    fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))
    radius = -1
    with pytest.raises(ValueError):
        task_func(ax, radius)
    plt.close()

def test_task_func_wrong_ax():
    fig, ax = plt.subplots()
    radius = 1
    with pytest.raises(TypeError):
        task_func(ax, radius)
    plt.close()