import pytest
from src_0677 import task_func
import pandas as pd

def test_task_func():
    df = pd.DataFrame({'team1': ['A', 'B', 'C'], 'team2': ['D', 'E', 'F'], 'score1': [1, 2, 3], 'score2': [4, 5, 6]})
    expected_df = pd.DataFrame({'team1': ['A', 'B', 'C'], 'team2': ['D', 'E', 'F'], 'score1': [1, 2, 3], 'score2': [4, 5, 6], 'winner': ['A', 'B', 'C']})
    assert task_func(df).equals(expected_df)

def test_task_func_ties():
    df = pd.DataFrame({'team1': ['A', 'B', 'C'], 'team2': ['D', 'E', 'F'], 'score1': [1, 2, 3], 'score2': [4, 5, 6]})
    expected_df = pd.DataFrame({'team1': ['A', 'B', 'C'], 'team2': ['D', 'E', 'F'], 'score1': [1, 2, 3], 'score2': [4, 5, 6], 'winner': ['A', 'B', 'C']})
    assert task_func(df).equals(expected_df)

def test_task_func_random_winner():
    df = pd.DataFrame({'team1': ['A', 'B', 'C'], 'team2': ['D', 'E', 'F'], 'score1': [1, 2, 3], 'score2': [4, 5, 6]})
    expected_df = pd.DataFrame({'team1': ['A', 'B', 'C'], 'team2': ['D', 'E', 'F'], 'score1': [1, 2, 3], 'score2': [4, 5, 6], 'winner': ['A', 'B', 'C']})
    assert task_func(df).equals(expected_df)