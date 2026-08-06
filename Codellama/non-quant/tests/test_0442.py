import pytest
from src_0442 import task_func
import numpy as np

def test_task_func():
    # Test that the function raises a TypeError if the inputs are not numpy arrays
    with pytest.raises(TypeError):
        task_func(1, 2)

    # Test that the function returns a valid result and 3D visualization
    P = np.array([[1, 2], [3, 4]])
    T = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    result, ax = task_func(P, T)
    assert isinstance(result, np.ndarray)
    assert isinstance(ax, plt.Axes3D)
    assert result.shape == (2, 3)
    assert ax.get_xlabel() == "x"
    assert ax.get_ylabel() == "y"
    assert ax.get_zlabel() == "z"