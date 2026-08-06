import pytest
from src_0047 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    # Create a sample dataframe
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50], 'C': [100, 200, 300, 400, 500]})

    # Test that the function returns a tuple with the expected values
    result, axes = task_func(df)
    assert isinstance(result, pd.DataFrame)
    assert isinstance(axes, np.ndarray)

    # Test that the function fills missing values with the column's average
    assert np.allclose(result['A'].mean(), result['A'].mean())
    assert np.allclose(result['B'].mean(), result['B'].mean())
    assert np.allclose(result['C'].mean(), result['C'].mean())

    # Test that the function computes Z-scores correctly
    assert np.allclose(result['A'].std(), 1)
    assert np.allclose(result['B'].std(), 1)
    assert np.allclose(result['C'].std(), 1)

    # Test that the function plots histograms for each numeric column
    assert len(axes) == 3
    assert axes[0].get_title() == 'A'
    assert axes[1].get_title() == 'B'
    assert axes[2].get_title() == 'C'