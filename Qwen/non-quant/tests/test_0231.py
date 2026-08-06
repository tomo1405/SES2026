import pytest
from src_0231 import task_func
import pandas as pd
import io
import matplotlib.pyplot as plt

@pytest.fixture
def sample_df():
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'Alice'],
        'Age': [25, 30, 35, 25],
        'Country': ['USA', 'Canada', 'UK', 'USA'],
        'Score': [88, 92, 87, 88]
    }
    return pd.DataFrame(data)

def test_task_func_invalid_input():
    assert task_func("not a dataframe") == "Invalid input"

def test_task_func_valid_input(sample_df):
    result = task_func(sample_df)
    assert isinstance(result, plt.Figure)

def test_task_func_duplicate_names(sample_df):
    # Adding a duplicate name with different score to check drop_duplicates
    sample_df.loc[len(sample_df)] = ['Alice', 40, 'Australia', 90]
    result = task_func(sample_df)
    assert isinstance(result, plt.Figure)

def test_task_func_empty_dataframe():
    empty_df = pd.DataFrame(columns=['Name', 'Age', 'Country', 'Score'])
    result = task_func(empty_df)
    assert isinstance(result, plt.Figure)

def test_task_func_no_data(sample_df):
    sample_df = sample_df.drop(columns=['Score'])
    result = task_func(sample_df)
    assert result == "Invalid input"