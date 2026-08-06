import pytest
from src_0677 import task_func
import pandas as pd
import random

# Mocking the random.choice function to ensure deterministic behavior in tests
class MockRandom:
    def choice(self, seq):
        return seq[0]

@pytest.fixture
def mock_random(monkeypatch):
    monkeypatch.setattr(random, 'choice', MockRandom().choice)

@pytest.fixture
def sample_df():
    data = {
        'team1': ['TeamA', 'TeamB', 'TeamC'],
        'team2': ['TeamD', 'TeamE', 'TeamF'],
        'score1': [10, 5, 8],
        'score2': [8, 5, 10]
    }
    return pd.DataFrame(data)

def test_task_func(mock_random, sample_df):
    result_df = task_func(sample_df)
    
    # Check if the 'winner' column is added
    assert 'winner' in result_df.columns
    
    # Check the correctness of the 'winner' values based on the scores
    expected_winners = ['TeamA', 'TeamE', 'TeamF']
    assert result_df['winner'].tolist() == expected_winners

def test_task_func_tie(mock_random, sample_df):
    # Create a scenario where all scores are equal
    sample_df['score1'] = [5, 5, 5]
    sample_df['score2'] = [5, 5, 5]
    
    result_df = task_func(sample_df)
    
    # Check if the 'winner' column is added
    assert 'winner' in result_df.columns
    
    # Since it's a tie and we mocked random.choice to always return the first element,
    # we expect the first team in each row to be the winner.
    expected_winners = ['TeamA', 'TeamB', 'TeamC']
    assert result_df['winner'].tolist() == expected_winners