import matplotlib.pyplot as plt
import numpy as np
import pytest

from src_0262 import task_func

def test_task_func():
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)
    ax = task_func(ax, 1)
    assert ax.get_rlabel_position() == 45
    assert ax.collections[0].get_paths()[0].vertices[:, 0].max() == 1
    with pytest.raises(ValueError):
        task_func(ax, -1)
    with pytest.raises(TypeError):
        task_func(fig, 1)