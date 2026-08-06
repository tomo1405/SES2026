import pytest
from src_0110 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import sys

# Mocking plt.show to capture the plot
def mock_show():
    pass

plt.show = mock_show

# Redirecting stdout to capture print statements
class CapturedOutput:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = self._stringio = BytesIO()
        return self

    def __exit__(self, *args):
        sys.stdout = self._original_stdout

@pytest.fixture
def sample_df():
    data = {
        'Item': ['apple', 'banana', 'grape', 'orange', 'pineapple'] * 3,
        'Location': ['store1', 'store2', 'store3'] * 5
    }
    return pd.DataFrame(data)

def test_task_func_invalid_df():
    with pytest.raises(ValueError):
        task_func(None)

def test_task_func_missing_columns():
    df = pd.DataFrame({'Item': [1, 2, 3], 'Price': [4, 5, 6]})
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_default_items_locations(sample_df):
    with CapturedOutput() as out:
        ax = task_func(sample_df)
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) > 0

def test_task_func_custom_items_locations(sample_df):
    items = ['apple', 'banana']
    locations = ['store1', 'store2']
    with CapturedOutput() as out:
        ax = task_func(sample_df, items=items, locations=locations)
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) > 0

def test_task_func_no_data(sample_df):
    sample_df = sample_df[sample_df['Item'] == 'nonexistent_item']
    with CapturedOutput() as out:
        ax = task_func(sample_df)
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == 0