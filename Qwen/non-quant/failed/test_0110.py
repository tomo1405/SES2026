import pytest
from src_0110 import task_func
import pandas as pd
import io
import sys

# Mocking plt.show to prevent actual plotting
class MockShow:
    def __call__(self):
        pass

@pytest.fixture
def mock_plt_show(monkeypatch):
    monkeypatch.setattr(plt, 'show', MockShow())

@pytest.fixture
def sample_df():
    data = {
        'Item': ['apple', 'banana', 'grape', 'orange', 'pineapple'] * 3,
        'Location': ['store1', 'store2', 'store3'] * 5
    }
    return pd.DataFrame(data)

def test_task_func_with_default_items_and_locations(sample_df, mock_plt_show):
    ax = task_func(sample_df)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_custom_items_and_locations(sample_df, mock_plt_show):
    custom_items = ['apple', 'banana']
    custom_locations = ['store1', 'store2']
    ax = task_func(sample_df, items=custom_items, locations=custom_locations)
    assert isinstance(ax, plt.Axes)

def test_task_func_invalid_dataframe_type(mock_plt_show):
    with pytest.raises(ValueError, match="Invalid 'df': must be a DataFrame with 'Item' and 'Location' columns."):
        task_func([1, 2, 3])

def test_task_func_missing_columns(mock_plt_show):
    data = {
        'Item': ['apple', 'banana'],
        'Price': [1.0, 0.5]
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError, match="Invalid 'df': must be a DataFrame with 'Item' and 'Location' columns."):
        task_func(df)