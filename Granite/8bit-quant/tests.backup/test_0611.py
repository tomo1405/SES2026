import pytest
from src_0611 import task_func
import pandas as pd
import seaborn as sns
from random import sample

# Constants
COLUMNS = ['A', 'B', 'C', 'D', 'E']

@pytest.fixture
def df():
    return pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [6, 7, 8, 9, 10],
        'C': [11, 12, 13, 14, 15],
        'D': [16, 17, 18, 19, 20],
        'E': [21, 22, 23, 24, 25]
    })

@pytest.fixture
def tuples():
    return [(1, 2), (3, 4)]

def test_task_func(df, tuples):
    # Test if the function returns a tuple of length 2
    result = task_func(df, tuples, 2)
    assert len(result) == 2

    # Test if the first element of the tuple is a DataFrame
    assert isinstance(result[0], pd.DataFrame)

    # Test if the second element of the tuple is a list
    assert isinstance(result[1], list)

def test_drop_rows(df, tuples):
    # Test if the function drops the specified rows from the DataFrame
    result_df = task_func(df, tuples, 0)[0]
    expected_df = df.set_index(list('ABCDE')).drop(tuples, errors='ignore').reset_index()
    assert result_df.equals(expected_df)

def test_generate_plots(df):
    # Test if the function generates plots for a non-empty DataFrame
    result_plots = task_func(df, [], 2)[1]
    assert len(result_plots) == 2
    assert all(isinstance(plot, sns.axisgrid.JointGrid) for plot in result_plots)

def test_empty_dataframe(df):
    # Test if the function returns an empty list of plots for an empty DataFrame
    result_plots = task_func(pd.DataFrame(), [], 2)[1]
    assert len(result_plots) == 0