import random

import numpy as np
from src_0254 import task_func


def test_task_func():

    # Mock the matplotlib axes object
    class Axes:
        def plot(self, x, y, color):
            assert isinstance(x, np.ndarray)
            assert isinstance(y, np.ndarray)
            assert color in COLORS

        def set_rlabel_position(self, position):
            assert 0 <= position <= 180

    ax = Axes()

    # Test with random inputs
    num_tests = 10
    for _ in range(num_tests):
        color = task_func(ax)
        assert color in COLORS

    # Test with specific inputs
    x = np.linspace(0, 2 * np.pi, 1000)
    y = np.sin(random.randint(1, 10)*x)
    color = random.choice(COLORS)
    ax.plot(x, y, color=color)
    ax.set_rlabel_position(random.randint(0, 180))