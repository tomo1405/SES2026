import numpy as np
import matplotlib.pyplot as plt
from src_0442 import task_func

def test_task_func():
    P = np.random.rand(10, 3)
    T = np.random.rand(3, 10, 3)
    result, ax = task_func(P, T)
    assert result.shape == (10, 10)
    assert isinstance(ax, plt.Axes)
    assert ax.name == "3d"