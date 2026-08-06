import pandas as pd
import matplotlib.pyplot as plt
import pytest

from src_1003 import task_func

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'target_column': [1, 2, 3, 4, 5],
        'other_column': ['a', 'b', 'c', 'd', 'e']
    })

def test_task_func(sample_data):
    df, ax = task_func(sample_data)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert 'target_column' in df.columns
    assert df['target_column'].dtype == 'int64'
    assert ax.get_title() == 'Histogram of target_column'
    assert ax.get_xlabel() == 'target_column'

def test_task_func_invalid_column(sample_data):
    with pytest.raises(ValueError):
        task_func(sample_data, 'invalid_column')

def test_task_func_invalid_data_type(sample_data):
    sample_data['target_column'] = sample_data['target_column'].astype('category')
    with pytest.raises(ValueError):
        task_func(sample_data)