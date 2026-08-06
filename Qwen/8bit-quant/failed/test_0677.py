import pytest
from src_0677 import task_func
import pandas as pd
import random

def test_task_func():
    # Test case 1: team1 wins
    data = {
        'team1': ['A', 'B'],
        'team2': ['C', 'D'],
        'score1': [3, 2],
        'score2': [1, 1]
    }
    df = pd.DataFrame(data)
    result_df = task_func(df)
    assert result_df['winner'].tolist() == ['A', 'B']

    # Test case 2: team2 wins
    data = {
        'team1': ['E', 'F'],
        'team2': ['G', 'H'],
        'score1': [1, 1],
        'score2': [3, 2]
    }
    df = pd.DataFrame(data)
    result_df = task_func(df)
    assert result_df['winner'].tolist() == ['G', 'H']

    # Test case 3: tie and random choice
    data = {
        'team1': ['I', 'J'],
        'team2': ['K', 'L'],
        'score1': [2, 2],
        'score2': [2, 2]
    }
    df = pd.DataFrame(data)
    result_df = task_func(df)
    assert result_df['winner'].isin(['I', 'K']).all() and result_df['winner'].isin(['J', 'L']).all()

    # Test case 4: empty DataFrame
    df = pd.DataFrame()
    result_df = task_func(df)
    assert result_df.empty

    # Test case 5: single row
    data = {
        'team1': ['M'],
        'team2': ['N'],
        'score1': [3],
        'score2': [2]
    }
    df = pd.DataFrame(data)
    result_df = task_func(df)
    assert result_df['winner'].tolist() == ['M']

# To ensure random.choice is predictable for testing purposes
@pytest.fixture(autouse=True)
def fix_randomness():
    random.seed(0)