import pytest
from src_0616 import task_func
import pandas as pd

def test_task_func_default_seed():
    expected_teams = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
    result_df = task_func(5, 3, rng_seed=42)
    
    assert isinstance(result_df, pd.DataFrame)
    assert list(result_df.columns) == ['Team', 'Match Result']
    assert list(result_df['Team']) == expected_teams

def test_task_func_no_seed():
    result_df = task_func(5, 3)
    assert isinstance(result_df, pd.DataFrame)
    assert list(result_df.columns) == ['Team', 'Match Result']
    assert len(result_df) == 5

def test_task_func_negative_goals_penalties():
    expected_teams = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
    result_df = task_func(-5, -3, rng_seed=42)
    
    assert isinstance(result_df, pd.DataFrame)
    assert list(result_df.columns) == ['Team', 'Match Result']
    assert list(result_df['Team']) == expected_teams

def test_task_func_zero_goals_penalties():
    expected_teams = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
    result_df = task_func(0, 0, rng_seed=42)
    
    assert isinstance(result_df, pd.DataFrame)
    assert list(result_df.columns) == ['Team', 'Match Result']
    assert list(result_df['Team']) == expected_teams

def test_task_func_large_numbers():
    expected_teams = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
    result_df = task_func(100, 100, rng_seed=42)
    
    assert isinstance(result_df, pd.DataFrame)
    assert list(result_df.columns) == ['Team', 'Match Result']
    assert list(result_df['Team']) == expected_teams