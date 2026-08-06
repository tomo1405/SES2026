import matplotlib.pyplot as plt
from src_0625 import task_func


def test_task_func_output_shape():
    # Test with a simple 3x2 array
    L = [[1, 2], [3, 4], [5, 6]]
    pca_result, ax = task_func(L)
    
    # Check if the PCA result has the correct shape
    assert pca_result.shape == (3, N_COMPONENTS)

def test_task_func_plot_type():
    # Test with a simple 3x2 array
    L = [[1, 2], [3, 4], [5, 6]]
    _, ax = task_func(L)
    
    # Check if the plot is of type AxesSubplot
    assert isinstance(ax, plt.Axes)

def test_task_func_with_zero_variance():
    # Test with a simple 3x2 array where one feature has zero variance
    L = [[1, 2], [1, 2], [1, 2]]
    pca_result, ax = task_func(L)
    
    # Check if the PCA result has the correct shape
    assert pca_result.shape == (3, N_COMPONENTS)

def test_task_func_with_negative_values():
    # Test with a simple 3x2 array containing negative values
    L = [[-1, -2], [-3, -4], [-5, -6]]
    pca_result, ax = task_func(L)
    
    # Check if the PCA result has the correct shape
    assert pca_result.shape == (3, N_COMPONENTS)

def test_task_func_with_single_point():
    # Test with a single point
    L = [[1, 2]]
    pca_result, ax = task_func(L)
    
    # Check if the PCA result has the correct shape
    assert pca_result.shape == (1, N_COMPONENTS)