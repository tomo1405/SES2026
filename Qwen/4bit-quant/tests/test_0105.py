import matplotlib.pyplot as plt
import pandas as pd
import pytest
from src_0105 import task_func


@pytest.fixture
def sample_data():
    data = {
        'group': ['A', 'A', 'B', 'B', 'C', 'C'],
        'date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-01', '2023-01-02', '2023-01-01', '2023-01-02']),
        'value': [10, 20, 30, 40, 50, 60]
    }
    return pd.DataFrame(data)

def test_task_func_valid_input(sample_data):
    ax = task_func(sample_data)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == 'Date (ordinal)'
    assert ax.get_ylabel() == 'Value'
    assert ax.get_title() == 'Scatterplot of Values for Each Group Over Time'

def test_task_func_invalid_df_type():
    with pytest.raises(ValueError):
        task_func([1, 2, 3])

def test_task_func_missing_columns():
    data = {
        'group': ['A', 'B'],
        'value': [10, 20]
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_empty_dataframe():
    df = pd.DataFrame(columns=['group', 'date', 'value'])
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_custom_groups(sample_data):
    ax = task_func(sample_data, groups=['A', 'B'])
    assert isinstance(ax, plt.Axes)
    # Additional checks can be added to verify specific behavior with custom groups