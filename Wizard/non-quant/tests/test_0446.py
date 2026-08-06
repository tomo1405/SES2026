python
import numpy as np
import pytest
from src_0446 import task_func

def test_task_func():
    points = np.array([[0, 0], [1, 1], [2, 2]])
    with pytest.raises(TypeError):
        task_func(points.tolist())
    with pytest.raises(ValueError):
        task_func(np.array([[0, 0], [1, 1]]))
    with pytest.raises(ValueError):
        task_func(np.array([[0, 0, 0], [1, 1, 1]]))
    vor, ax = task_func(points)
    assert isinstance(vor, Voronoi)
    assert isinstance(ax, plt.Axes)