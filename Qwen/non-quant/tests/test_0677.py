import pytest
from src_0677 import task_func
import pandas as pd

@pytest.fixture
def sample_df():
    data = {
        'team1': ['A', 'B', 'C'],
        'team2': ['X', 'Y', 'Z'],
        'score1': [3, 2, 1],
        'score2': [1, 2, 3]
    }
    return pd.DataFrame(data)

def test_task_func(sample_df):
    result_df = task_func(sample_df)
    
    # Check if the 'winner' column is added
    assert 'winner' in result_df.columns
    
    # Check if the winners are determined correctly
    expected_winners = ['A', 'Y', 'Z']
    assert all(result_df['winner'] == expected_winners)

def test_task_func_tie(sample_df):
    # Modify scores to create a tie situation
    sample_df.loc[0, 'score1'] = 2
    sample_df.loc[0, 'score2'] = 2
    
    result_df = task_func(sample_df)
    
    # Check if the 'winner' column is added
    assert 'winner' in result_df.columns
    
    # Check if the tie is handled correctly (random choice)
    winner = result_df.loc[0, 'winner']
    assert winner in ['A', 'X']

def test_task_func_empty_df():
    empty_df = pd.DataFrame(columns=['team1', 'team2', 'score1', 'score2'])
    result_df = task_func(empty_df)
    
    # Check if the 'winner' column is added
    assert 'winner' in result_df.columns
    
    # Check if the DataFrame remains empty
    assert result_df.empty