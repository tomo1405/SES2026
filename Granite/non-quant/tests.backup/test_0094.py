import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from src_0094 import task_func
import pytest

def test_task_func_invalid_n_components():
    with pytest.raises(ValueError) as excinfo:
        task_func(np.random.rand(10, 10), n_components=-1)
    assert "n_components must be a positive integer" in str(excinfo.value)

def test_task_func_invalid_data():
    with pytest.raises(ValueError) as excinfo:
        task_func("invalid data")
    assert "Input data must be a 2D numpy array or a pandas DataFrame" in str(excinfo.value)

def test_task_func_valid_input():
    data = np.random.rand(100, 10)
    transformed_data, ax = task_func(data)
    assert isinstance(transformed_data, pd.DataFrame)
    assert transformed_data.shape == (100, 2)
    assert isinstance(ax, plt.Axes)