import pytest
from src_0639 import task_func
import numpy as np
import pandas as pd

def test_task_func_default_parameters():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (5, 100)
    assert all(isinstance(team, str) and team.startswith('Team') for team in df.index)
    assert all(isinstance(game, str) and game.startswith('Game') for game in df.columns)
    assert df.values.min() >= 0
    assert df.values.max() <= 100

def test_task_func_custom_parameters():
    num_teams = 3
    num_games = 50
    df = task_func(num_teams=num_teams, num_games=num_games)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (num_teams, num_games)
    assert all(isinstance(team, str) and team.startswith('Team') for team in df.index)
    assert all(isinstance(game, str) and game.startswith('Game') for game in df.columns)
    assert df.values.min() >= 0
    assert df.values.max() <= 100

def test_task_func_no_teams():
    with pytest.raises(ValueError):
        task_func(num_teams=0)

def test_task_func_no_games():
    with pytest.raises(ValueError):
        task_func(num_games=0)

def test_task_func_negative_teams():
    with pytest.raises(ValueError):
        task_func(num_teams=-1)

def test_task_func_negative_games():
    with pytest.raises(ValueError):
        task_func(num_games=-1)