import pytest
from src_0611 import task_func
import pandas as pd
import seaborn as sns

# Constants
COLUMNS = ['A', 'B', 'C', 'D', 'E']

@pytest.fixture
def df():
    return pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [1, 2, 3, 4, 5],
        'D': [5, 4, 3, 2, 1],
        'E': [1, 2, 3, 4, 5]
    })

@pytest.fixture
def tuples():
    return [(1, 2), (3, 4)]

def test_task_func(df, tuples):
    # Test if the function returns a tuple of two elements
    result = task_func(df, tuples, 2)
    assert len(result) == 2

    # Test if the first element of the returned tuple is a DataFrame
    assert isinstance(result[0], pd.DataFrame)

    # Test if the second element of the returned tuple is a list
    assert isinstance(result[1], list)

    # Test if the plots are of type seaborn.axisgrid.JointGrid
    for plot in result[1]:
        assert isinstance(plot, sns.axisgrid.JointGrid)

def test_task_func_with_empty_df(df, tuples):
    # Test if the function returns a tuple of two elements
    # even if the DataFrame is empty
    df = pd.DataFrame()
    result = task_func(df, tuples, 2)
    assert len(result) == 2

    # Test if the first element of the returned tuple is an empty DataFrame
    assert result[0].empty

    # Test if the second element of the returned tuple is an empty list
    assert not result[1]