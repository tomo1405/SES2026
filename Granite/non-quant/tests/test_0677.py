import pandas as pd
import random
import pytest
from src_0677 import task_func

@pytest.fixture
def sample_df():
    data = {
        'team1': ['Team A', 'Team B', 'Team C', 'Team D'],
        'team2': ['Team E', 'Team F', 'Team G', 'Team H'],
        'score1': [10, 20, 15, 25],
        'score2': [5, 15, 10, 20]
    }
    return pd.DataFrame(data)

def test_task_func(sample_df):
    result_df = task_func(sample_df)
    assert 'winner' in result_df.columns
    assert len(result_df) == len(sample_df)
    for index, row in result_df.iterrows():
        assert row['winner'] in [row['team1'], row['team2']]

def test_determine_winner(sample_df):
    winner_series = pd.Series([task_func.determine_winner(row) for index, row in sample_df.iterrows()], index=sample_df.index)
    for index, row in sample_df.iterrows():
        if row['score1'] > row['score2']:
            assert winner_series[index] == row['team1']
        elif row['score1'] < row['score2']:
            assert winner_series[index] == row['team2']
        else:
            assert winner_series[index] in [row['team1'], row['team2']]