import pytest
from src_0617 import task_func

def test_task_func():
    goals = 10
    penalties = 5
    results_df, ax = task_func(goals, penalties)
    assert isinstance(results_df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert len(results_df) == len(task_func.TEAMS)
    assert all(results_df['Goals'] >= 0)
    assert all(results_df['Penalty Cost'] >= 0)
    assert ax.get_xlabel() == 'Team'
    assert ax.get_ylabel() == 'Results'
    assert ax.get_title() == 'Match Results'

def test_task_func_with_seed():
    goals = 10
    penalties = 5
    rng_seed = 42
    results_df, ax = task_func(goals, penalties, rng_seed=rng_seed)
    assert isinstance(results_df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert len(results_df) == len(task_func.TEAMS)
    assert all(results_df['Goals'] >= 0)
    assert all(results_df['Penalty Cost'] >= 0)
    assert ax.get_xlabel() == 'Team'
    assert ax.get_ylabel() == 'Results'
    assert ax.get_title() == 'Match Results'

def test_task_func_with_negative_goals_and_penalties():
    goals = -10
    penalties = -5
    results_df, ax = task_func(goals, penalties)
    assert isinstance(results_df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert len(results_df) == len(task_func.TEAMS)
    assert all(results_df['Goals'] >= 0)
    assert all(results_df['Penalty Cost'] >= 0)
    assert ax.get_xlabel() == 'Team'
    assert ax.get_ylabel() == 'Results'
    assert ax.get_title() == 'Match Results'

def test_task_func_with_zero_goals_and_penalties():
    goals = 0
    penalties = 0
    results_df, ax = task_func(goals, penalties)
    assert isinstance(results_df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert len(results_df) == len(task_func.TEAMS)
    assert all(results_df['Goals'] >= 0)
    assert all(results_df['Penalty Cost'] >= 0)
    assert ax.get_xlabel() == 'Team'
    assert ax.get_ylabel() == 'Results'
    assert ax.get_title() == 'Match Results'