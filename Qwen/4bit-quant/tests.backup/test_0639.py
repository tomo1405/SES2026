import pytest
from src_0639 import task_func
import numpy as np
import pandas as pd

def test_task_func_default_values():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (5, 100)
    assert all(df.index == ['Team1', 'Team2', 'Team3', 'Team4', 'Team5'])
    assert all(df.columns == [f'Game{i}' for i in range(1, 101)])

def test_task_func_custom_values():
    num_teams = 3
    num_games = 50
    df = task_func(num_teams, num_games)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (num_teams, num_games)
    assert all(df.index == [f'Team{i}' for i in range(1, num_teams + 1)])
    assert all(df.columns == [f'Game{i}' for i in range(1, num_games + 1)])

def test_task_func_scores_range():
    df = task_func()
    assert df.values.min() >= 0
    assert df.values.max() <= 100

def test_task_func_randomness():
    df1 = task_func()
    df2 = task_func()
    assert not df1.equals(df2), "The generated DataFrames should be different due to randomness"