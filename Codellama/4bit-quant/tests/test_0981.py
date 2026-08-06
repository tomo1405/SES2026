import pytest
from src_0981 import task_func
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

def test_task_func():
    # Test case 1: No numeric columns present
    df = pd.DataFrame({'A': ['a', 'b', 'c'], 'B': [1, 2, 3]})
    with pytest.raises(ValueError):
        task_func(df)

    # Test case 2: Numeric columns present, but no correlation
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df, fig = task_func(df)
    assert isinstance(fig, plt.Figure)
    assert np.allclose(df.corr(), np.array([[1., 0.], [0., 1.]]))

    # Test case 3: Numeric columns present, correlation present
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    df, fig = task_func(df)
    assert isinstance(fig, plt.Figure)
    assert np.allclose(df.corr(), np.array([[1., 0.866, 0.], [0., 1., 0.], [0., 0., 1.]]))

    # Test case 4: Numeric columns present, correlation present, scaling applied
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    df, fig = task_func(df)
    assert isinstance(fig, plt.Figure)
    assert np.allclose(df.corr(), np.array([[1., 0.866, 0.], [0., 1., 0.], [0., 0., 1.]]))
    assert np.allclose(df.mean(), np.array([2., 5., 8.]))
    assert np.allclose(df.std(), np.array([1., 1., 1.]))