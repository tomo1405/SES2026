import pytest
from src_0617 import task_func
import pandas as pd
import matplotlib.pyplot as plt

@pytest.fixture
def setup():
    plt.close('all')  # Close any open plots to avoid interference between tests

def test_task_func_default_parameters(setup):
    goals = 5
    penalties = 3
    results_df, ax = task_func(goals, penalties)
    
    assert isinstance(results_df, pd.DataFrame)
    assert results_df.shape == (5, 3)  # 5 teams, 3 columns
    assert all(results_df['Goals'] >= 0)
    assert all(results_df['Penalty Cost'] >= 0)
    assert isinstance(ax, plt.Axes)

def test_task_func_custom_teams_and_penalty_cost(setup):
    goals = 10
    penalties = 2
    custom_teams = ['Team X', 'Team Y']
    custom_penalty_cost = 500
    results_df, ax = task_func(goals, penalties, teams=custom_teams, penalty_cost=custom_penalty_cost)
    
    assert isinstance(results_df, pd.DataFrame)
    assert results_df.shape == (2, 3)  # 2 teams, 3 columns
    assert all(results_df['Goals'] >= 0)
    assert all(results_df['Penalty Cost'] <= custom_penalty_cost * penalties)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_rng_seed(setup):
    goals = 7
    penalties = 4
    rng_seed = 42
    results_df1, _ = task_func(goals, penalties, rng_seed=rng_seed)
    results_df2, _ = task_func(goals, penalties, rng_seed=rng_seed)
    
    assert results_df1.equals(results_df2)

def test_task_func_negative_inputs(setup):
    goals = -5
    penalties = -3
    results_df, ax = task_func(goals, penalties)
    
    assert isinstance(results_df, pd.DataFrame)
    assert results_df.shape == (5, 3)  # 5 teams, 3 columns
    assert all(results_df['Goals'] >= 0)
    assert all(results_df['Penalty Cost'] >= 0)
    assert isinstance(ax, plt.Axes)