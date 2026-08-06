import numpy as np
import pandas as pd
import pytest
import seaborn as sns
from src_0158 import task_func


def test_task_func():
    # Test case 1: Input data is a 2D numpy array
    data = np.array([[1, 2, 3], [4, 5, 6]])
    df, ax = task_func(data)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, sns.heatmap)
    assert df.shape == (2, 4)
    assert ax.shape == (2, 2)

    # Test case 2: Input data is not a 2D numpy array
    data = np.array([1, 2, 3])
    with pytest.raises(ValueError):
        task_func(data)

    # Test case 3: Input data is a 2D numpy array with invalid dimensions
    data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    with pytest.raises(ValueError):
        task_func(data)

    # Test case 4: Input data is a 2D numpy array with invalid dimensions
    data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    with pytest.raises(ValueError):
        task_func(data)

    # Test case 5: Input data is a 2D numpy array with invalid dimensions
    data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    with pytest.raises(ValueError):
        task_func(data)

    # Test case 6: Input data is a 2D numpy array with invalid dimensions
    data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    with pytest.raises(ValueError):
        task_func(data)

    # Test case 7: Input data is a 2D numpy array with invalid dimensions
    data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    with pytest.raises(ValueError):
        task_func(data)

    # Test case 8: Input data is a 2D numpy array with invalid dimensions
    data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    with pytest.raises(ValueError):
        task_func(data)

    # Test case 9: Input data is a 2D numpy array with invalid dimensions
    data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    with pytest.raises(ValueError):
        task_func(data)

    # Test case 10: Input data is a 2D numpy array with invalid dimensions
    data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    with pytest.raises(ValueError):
        task_func(data)