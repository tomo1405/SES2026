import pytest
from src_0618 import task_func
import pandas as pd
import numpy as np

def test_task_func_basic():
    rng_seed = 42
    goals = 5
    penalties = 3
    expected_teams = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
    
    df = task_func(goals, penalties, rng_seed=rng_seed)
    
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == ['Team', 'Match Result', 'Goals', 'Penalty Cost']
    assert all(df['Team'].isin(expected_teams))
    
    # Check that the number of rows matches the number of teams
    assert len(df) == len(expected_teams)
    
    # Check that the values are within the expected range
    assert all(df['Goals'] <= goals)
    assert all(df['Penalty Cost'] <= penalties * 1000)

def test_task_func_no_teams():
    rng_seed = 42
    goals = 5
    penalties = 3
    teams = []
    
    df = task_func(goals, penalties, rng_seed=rng_seed, teams=teams)
    
    assert df.empty

def test_task_func_single_team():
    rng_seed = 42
    goals = 5
    penalties = 3
    teams = ['Team X']
    
    df = task_func(goals, penalties, rng_seed=rng_seed, teams=teams)
    
    assert len(df) == 1
    assert df.iloc[0]['Team'] == 'Team X'

def test_task_func_randomness():
    rng_seed = 42
    goals = 5
    penalties = 3
    
    df1 = task_func(goals, penalties, rng_seed=rng_seed)
    df2 = task_func(goals, penalties, rng_seed=rng_seed)
    
    assert df1.equals(df2)

def test_task_func_no_penalties():
    rng_seed = 42
    goals = 5
    penalties = 0
    
    df = task_func(goals, penalties, rng_seed=rng_seed)
    
    assert all(df['Penalty Cost'] == 0)