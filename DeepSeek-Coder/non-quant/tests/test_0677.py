import pytest
from src_0677 import task_func
import pandas as pd
import random

# Mock data for testing
data = {
    'team1': ['TeamA', 'TeamB', 'TeamC'],
    'team2': ['TeamX', 'TeamY', 'TeamZ'],
    'score1': [2, 3, 1],
    'score2': [1, 2, 3],
    'team1': ['TeamA', 'TeamB', 'TeamC'],
    'team2': ['TeamX', 'TeamY', 'TeamZ']
}

df = pd.DataFrame(data)

def test_task_func():
    result = task_func(df)
    assert 'winner' in result.columns
    assert len(result) == 3
    assert result['winner'].iloc[0] in ['TeamA', 'TeamX']
    assert result['winner'].iloc[1] in ['TeamB', 'TeamY']
    assert result['winner'].iloc[2] in ['TeamC', 'TeamZ']