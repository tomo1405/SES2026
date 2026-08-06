import pytest
from src_0617 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func_defaults():
    results_df, ax = task_func(5, 3)
    assert isinstance(results_df, pd.DataFrame)
    assert len(results_df) == 5
    assert all(col in results_df.columns for col in ['Team', 'Goals', 'Penalty Cost'])
    plt.close(ax.figure)

def test_task_func_with_seed():
    results_df1, _ = task_func(5, 3, rng_seed=42)
    results_df2, _ = task_func(5, 3, rng_seed=42)
    assert results_df1.equals(results_df2)

def test_task_func_custom_teams():
    custom_teams = ['Team X', 'Team Y']
    results_df, _ = task_func(5, 3, teams=custom_teams)
    assert len(results_df) == 2
    assert all(team in results_df['Team'].values for team in custom_teams)
    plt.close(ax.figure)

def test_task_func_custom_penalty_cost():
    custom_penalty_cost = 500
    results_df, _ = task_func(5, 3, penalty_cost=custom_penalty_cost)
    assert results_df['Penalty Cost'].max() <= custom_penalty_cost * 3
    plt.close(ax.figure)

def test_task_func_negative_goals_penalties():
    results_df, _ = task_func(-5, -3)
    assert results_df['Goals'].min() >= 0
    assert results_df['Penalty Cost'].min() >= 0
    plt.close(ax.figure)