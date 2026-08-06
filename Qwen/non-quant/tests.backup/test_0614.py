import pytest
from src_0614 import task_func

def test_task_func_with_no_teams():
    goals = {}
    penalties = {}
    expected_df = pd.DataFrame(columns=['Team', 'Score'])
    result_df = task_func(goals, penalties)
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_with_all_teams():
    goals = {'Team A': 5, 'Team B': 3, 'Team C': 7, 'Team D': 2, 'Team E': 4}
    penalties = {'Team A': 2, 'Team B': 1, 'Team C': 3, 'Team D': 0, 'Team E': 5}
    expected_df = pd.DataFrame({
        'Team': ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'],
        'Score': [3, 2, 4, 2, -1]
    })
    result_df = task_func(goals, penalties)
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_with_negative_goals():
    goals = {'Team A': -5, 'Team B': 0, 'Team C': 5}
    penalties = {'Team A': 0, 'Team B': 0, 'Team C': 0}
    expected_df = pd.DataFrame({
        'Team': ['Team A', 'Team B', 'Team C'],
        'Score': [-5, 0, 5]
    })
    result_df = task_func(goals, penalties)
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_with_exceeding_goals_range():
    goals = {'Team A': 15, 'Team B': -15}
    penalties = {'Team A': 0, 'Team B': 0}
    expected_df = pd.DataFrame({
        'Team': ['Team A', 'Team B'],
        'Score': [10, -10]
    })
    result_df = task_func(goals, penalties)
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_with_missing_teams():
    goals = {'Team A': 5, 'Team C': 7}
    penalties = {'Team B': 1, 'Team D': 0}
    expected_df = pd.DataFrame({
        'Team': ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'],
        'Score': [5, -1, 7, 0, 0]
    })
    result_df = task_func(goals, penalties)
    pd.testing.assert_frame_equal(result_df, expected_df)