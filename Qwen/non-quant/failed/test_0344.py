import pytest
from src_0344 import task_func
import pandas as pd

@pytest.fixture
def sample_df():
    data = {
        'category': ['A', 'B', 'A', 'C', 'B', 'A', 'D', 'C', 'B', 'A']
    }
    return pd.DataFrame(data)

def test_task_func_with_valid_data(sample_df):
    ax = task_func(sample_df, 'category', 'Category Distribution')
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == 4  # There should be 4 unique categories: A, B, C, D

def test_task_func_with_empty_dataframe():
    with pytest.raises(ValueError) as excinfo:
        task_func(pd.DataFrame(), 'category')
    assert str(excinfo.value) == "The DataFrame is empty or the specified column does not exist."

def test_task_func_with_nonexistent_column(sample_df):
    with pytest.raises(ValueError) as excinfo:
        task_func(sample_df, 'nonexistent_column')
    assert str(excinfo.value) == "The DataFrame is empty or the specified column does not exist."

def test_task_func_with_no_title(sample_df):
    ax = task_func(sample_df, 'category')
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == ''  # No title should be set

def test_task_func_with_single_value_in_column(sample_df):
    single_value_df = pd.DataFrame({'category': ['A'] * 10})
    ax = task_func(single_value_df, 'category', 'Single Value Distribution')
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == 1  # There should be only one unique category: A