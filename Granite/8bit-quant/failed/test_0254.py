import pytest
from src_0254 import task_func

def test_task_func():
    import numpy as np
    import random

    # Mock the matplotlib Axes object
    class MockAxes:
        def plot(self, x, y, color):
            assert isinstance(x, np.ndarray)
            assert isinstance(y, np.ndarray)
            assert color in COLORS

        def set_rlabel_position(self, position):
            assert 0 <= position <= 180

    # Test with different values of rlabel_position
    for _ in range(10):
        ax = MockAxes()
        color = task_func(ax)
        assert color in COLORS