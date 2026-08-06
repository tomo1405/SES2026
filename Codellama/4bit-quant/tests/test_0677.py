import pandas as pd
from src_0677 import task_func


def test_task_func():
    df = pd.DataFrame({'team1': ['A', 'B', 'C'], 'team2': ['D', 'E', 'F'], 'score1': [10, 20, 30], 'score2': [15, 25, 35]})
    expected_df = pd.DataFrame({'team1': ['A', 'B', 'C'], 'team2': ['D', 'E', 'F'], 'score1': [10, 20, 30], 'score2': [15, 25, 35], 'winner': ['A', 'B', 'C']})
    actual_df = task_func(df)
    assert actual_df.equals(expected_df)