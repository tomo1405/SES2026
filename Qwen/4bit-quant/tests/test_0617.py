import pytest
from src_0617 import task_func
import pandas as pd
import numpy as np

def test_task_func_defaults():
    goals = 5
    penalties = 3
    expected_teams = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
    
    results_df, ax = task_func(goals, penalties)
    
    assert isinstance(results_df, pd.DataFrame)
    assert len(results_df) == len(expected_teams)
    assert all(team in results_df['Team'].values for team in expected_teams)
    assert all(isinstance(goal, int) for goal in results_df['Goals'])
    assert all(isinstance(penalty_cost, int) for penalty_cost in results_df['Penalty Cost'])

def test_task_func_with_custom_teams():
    goals = 5
    penalties = 3
    custom_teams = ['Custom Team 1', 'Custom Team 2']
    
    results_df, ax = task_func(goals, penalties, teams=custom_teams)
    
    assert isinstance(results_df, pd.DataFrame)
    assert len(results_df) == len(custom_teams)
    assert all(team in results_df['Team'].values for team in custom_teams)

def test_task_func_with_custom_penalty_cost():
    goals = 5
    penalties = 3
    custom_penalty_cost = 500
    
    results_df, ax = task_func(goals, penalties, penalty_cost=custom_penalty_cost)
    
    assert isinstance(results_df, pd.DataFrame)
    assert all(penalty_cost % custom_penalty_cost == 0 for penalty_cost in results_df['Penalty Cost'])

def test_task_func_with_rng_seed():
    goals = 5
    penalties = 3
    rng_seed = 42
    results_df1, _ = task_func(goals, penalties, rng_seed=rng_seed)
    results_df2, _ = task_func(goals, penalties, rng_seed=rng_seed)
    
    assert results_df1.equals(results_df2)

def test_task_func_negative_inputs():
    goals = -5
    penalties = -3
    
    results_df, ax = task_func(goals, penalties)
    
    assert all(isinstance(goal, int) for goal in results_df['Goals'])
    assert all(isinstance(penalty_cost, int) for penalty_cost in results_df['Penalty Cost'])