import pytest
from src_0258 import task_func
import numpy as np
import math

def test_task_func():
    ax = task_func(np.linspace(0, 10 * 2 * math.pi, 1000), 10)
    assert ax.get_rlabel_position() == 10 * 45
    assert len(ax.get_lines()) == 1
    assert ax.get_lines()[0].get_xdata().shape == (1000,)
    assert ax.get_lines()[0].get_ydata().shape == (1000,)

if __name__ == '__main__':
    pytest.main()