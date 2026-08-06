python
import random
import datetime
import matplotlib.pyplot as plt
import pytest

from src_0494 import task_func

def test_task_func():
    with pytest.raises(TypeError):
        task_func(1234567890, teams=123)

    with pytest.raises(ValueError):
        task_func(1234567890000)

    performance_data, fig = task_func(1611134400000)

    assert isinstance(performance_data, dict)
    assert all(isinstance(t, str) for t in performance_data.keys())
    assert all(isinstance(p, list) for p in performance_data.values())
    assert all(isinstance(d, float) for p in performance_data.values() for d in p)

    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 1
    assert isinstance(fig.axes[0], plt.Axes)
    assert fig.axes[0].get_xlabel() == "Days since 2021-01-01 00:00:00"
    assert fig.axes[0].get_ylabel() == "Performance"
    assert len(fig.axes[0].lines) == 5
    assert all(isinstance(l, plt.Line2D) for l in fig.axes[0].lines)
    assert all(l.get_label() in performance_data.keys() for l in fig.axes[0].lines)
    assert all(len(l.get_data()[0]) == len(l.get_data()[1]) for l in fig.axes[0].lines)