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