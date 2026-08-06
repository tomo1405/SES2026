import pytest
from src_0092 import task_func
import pandas as pd
import numpy as np

@pytest.fixture
def sample_data():
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [2, 3, 5, 7, 11]
    }
    return pd.DataFrame(data)

def test_task_func_valid_columns(sample_data):
    result, ax = task_func(sample_data, 'A', 'B')
    assert isinstance(result, tuple)
    assert len(result) == 5
    assert isinstance(ax, plt.Axes)

def test_task_func_invalid_column(sample_data):
    with pytest.raises(ValueError):
        task_func(sample_data, 'A', 'C')

def test_task_func_empty_dataframe():
    empty_df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(empty_df, 'A', 'B')

def test_task_func_single_row_dataframe():
    single_row_df = pd.DataFrame({'A': [1], 'B': [2]})
    result, ax = task_func(single_row_df, 'A', 'B')
    assert result[0] is np.nan  # Slope
    assert result[1] is np.nan  # Intercept
    assert result[2] is np.nan  # R-value
    assert result[3] is np.nan  # P-value
    assert result[4] is np.nan  # Standard error
    assert isinstance(ax, plt.Axes)

def test_task_func_identical_values():
    identical_values_df = pd.DataFrame({'A': [1, 1, 1], 'B': [1, 1, 1]})
    result, ax = task_func(identical_values_df, 'A', 'B')
    assert result[0] == 0  # Slope
    assert result[1] == 1  # Intercept
    assert result[2] == 1  # R-value
    assert result[3] == 1  # P-value
    assert np.isinf(result[4])  # Standard error (division by zero)
    assert isinstance(ax, plt.Axes)