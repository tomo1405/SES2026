import pytest
from src_0677 import task_func
import pandas as pd

def test_task_func():
    # Create a sample dataframe
    df = pd.DataFrame({'team1': ['A', 'B', 'C'], 'team2': ['D', 'E', 'F'], 'score1': [1, 2, 3], 'score2': [4, 5, 6]})

    # Test the function with the sample dataframe
    result = task_func(df)

    # Check that the 'winner' column is created and has the correct values
    assert 'winner' in result.columns
    assert (result['winner'] == ['A', 'B', 'C']).all()

    # Check that the original dataframe is not modified
    assert df.equals(pd.DataFrame({'team1': ['A', 'B', 'C'], 'team2': ['D', 'E', 'F'], 'score1': [1, 2, 3], 'score2': [4, 5, 6]}))