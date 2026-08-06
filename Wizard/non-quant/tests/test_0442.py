python
import numpy as np
import matplotlib.pyplot as plt
import pytest

def task_func(P, T):
    if not (isinstance(P, np.ndarray) and isinstance(T, np.ndarray)):
        raise TypeError("Expected inputs to be numpy arrays")

    # Compute the matrix-tensor product to ensure the result has the desired shape
    result = np.einsum("ij,jkl->ik", P, T)

    # Visualize the result in 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(result[:, 0], result[:, 1], result[:, 2])

    # Return the result and the 3D visualization
    return result, ax

# Test the function with valid inputs
def test_task_func_valid_inputs():
    P = np.array([[1, 2, 3], [4, 5, 6]])
    T = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    result, ax = task_func(P, T)
    assert result.shape == (2, 3)
    assert isinstance(ax, plt.Axes)

# Test the function with invalid inputs
def test_task_func_invalid_inputs():
    P = "not a numpy array"
    T = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    with pytest.raises(TypeError):
        task_func(P, T)

# Test the function with invalid inputs
def test_task_func_invalid_inputs_2():
    P = np.array([[1, 2, 3], [4, 5, 6]])
    T = "not a numpy array"
    with pytest.raises(TypeError):
        task_func(P, T)