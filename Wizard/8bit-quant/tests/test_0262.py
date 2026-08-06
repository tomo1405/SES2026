python
import pytest
import matplotlib.pyplot as plt
import numpy as np

def task_func(ax, radius):
    if radius < 0:
        raise ValueError('Radius must be non-negative')
    if not isinstance(ax, plt.PolarAxes):
        raise TypeError('ax must be a polar plot')

    theta = np.linspace(0, 2 * np.pi, 1000)
    ax.plot(theta, radius * np.ones_like(theta))
    ax.set_rlabel_position(radius * 45)
    return ax

def test_task_func():
    fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))
    task_func(ax, 1)
    assert ax.get_rlabel_position() == 45
    assert ax.lines[0].get_ydata()[0] == 1
    assert ax.lines[0].get_xdata()[0] == 0
    assert ax.lines[0].get_xdata()[-1] == 6.283185307179586
    assert ax.lines[0].get_ydata()[-1] == 1

    with pytest.raises(ValueError):
        task_func(ax, -1)

    with pytest.raises(TypeError):
        task_func(plt.subplot(111), 1)