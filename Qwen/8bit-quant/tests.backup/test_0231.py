import pytest
from src_0231 import task_func
import pandas as pd
import matplotlib.pyplot as plt

@pytest.fixture
def sample_df():
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'Alice'],
        'Age': [25, 30, 35, 25],
        'Country': ['USA', 'Canada', 'UK', 'USA'],
        'Score': [85, 90, 78, 85]
    }
    return pd.DataFrame(data)

def test_task_func_valid_input(sample_df):
    result = task_func(sample_df)
    assert isinstance(result, plt.Figure)
    plt.close(result)

def test_task_func_invalid_input():
    result = task_func("not a dataframe")
    assert result == "Invalid input"

def test_task_func_no_duplicates(sample_df):
    # Remove duplicates manually to simulate a case where there are no duplicates
    sample_df = sample_df.drop_duplicates(subset='Name')
    result = task_func(sample_df)
    assert isinstance(result, plt.Figure)
    plt.close(result)

def test_task_func_empty_dataframe():
    empty_df = pd.DataFrame(columns=['Name', 'Age', 'Country', 'Score'])
    result = task_func(empty_df)
    assert isinstance(result, plt.Figure)
    plt.close(result)