import pytest
from src_0102 import task_func

def test_task_func():
    # Test 1: Check if the function returns a valid matplotlib Axes object
    ax = task_func()
    assert isinstance(ax, matplotlib.axes.Axes)

    # Test 2: Check if the function raises an error when the data_url is invalid
    with pytest.raises(ValueError):
        task_func(data_url="invalid_url")

    # Test 3: Check if the function raises an error when the seed is invalid
    with pytest.raises(ValueError):
        task_func(seed="invalid_seed")

    # Test 4: Check if the function returns the correct correlation matrix
    expected_corr = np.array([[1.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.1, 0.2],
                              [0.1, 1.0, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.1, 0.2],
                              [0.2, 0.2, 1.0, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.1, 0.2],
                              [0.3, 0.3, 0.3, 1.0, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.1, 0.2],
                              [0.4, 0.4, 0.4, 0.4, 1.0, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.1, 0.2],
                              [0.5, 0.5, 0.5, 0.5, 0.5, 1.0, 0.6, 0.7, 0.8, 0.9, 1.0, 0.1, 0.2],
                              [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 1.0, 0.7, 0.8, 0.9, 1.0, 0.1, 0.2],
                              [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 1.0, 0.8, 0.9, 1.0, 0.1, 0.2],
                              [0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 1.0, 0.9, 1.0, 0.1, 0.2],
                              [0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 1.0, 1.0, 0.1, 0.2],
                              [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.1, 0.2],
                              [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 1.0, 0.2],
                              [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 1.0]])
    corr = task_func().corr()
    assert np.allclose(corr, expected_corr)