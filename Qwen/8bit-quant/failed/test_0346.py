import pytest
from src_0346 import task_func
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1]
    })

def test_task_func_valid_input(sample_df):
    ax = task_func(sample_df, 'A', 'B')
    assert isinstance(ax, sns.axisgrid.FacetGrid)

def test_task_func_invalid_dataframe():
    with pytest.raises(ValueError):
        task_func(None, 'A', 'B')

def test_task_func_empty_dataframe():
    with pytest.raises(ValueError):
        task_func(pd.DataFrame(), 'A', 'B')

def test_task_func_missing_column(sample_df):
    with pytest.raises(ValueError):
        task_func(sample_df, 'C', 'B')

def test_task_func_missing_second_column(sample_df):
    with pytest.raises(ValueError):
        task_func(sample_df, 'A', 'C')