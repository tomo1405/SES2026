import pytest
from src_0254 import task_func
import numpy as np
import random

COLORS = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

def test_task_func():
    ax = np.linspace(0, 2 * np.pi, 1000)
    y = np.sin(random.randint(1, 10)*x)

    color = task_func(ax)

    assert color in COLORS
    assert ax.get_rlabel_position() in range(0, 180)