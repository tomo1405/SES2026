import pytest
from src_0614 import task_func

def test_task_func():
    goals = {
        'Team A': 5,
        'Team B': 3,
        'Team C': -2,
        'Team D': 8,
        'Team E': -1
    }
    penalties = {
        'Team A': 2,
        'Team B': 1,
        'Team C': 3,
        'Team D': 5,
        'Team E': 4
    }

    expected_output = pd.DataFrame({
        'Team': ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'],
        'Score': [3, 2, -5, 3, -5]
    })

    result = task_func(goals, penalties)

    # Check if the DataFrame has the correct columns
    assert list(result.columns) == ['Team', 'Score']

    # Check if the DataFrame has the correct number of rows
    assert len(result) == 5

    # Check if the scores are correctly calculated and clipped
    for i, row in expected_output.iterrows():
        assert result.loc[i, 'Team'] == row['Team']
        assert result.loc[i, 'Score'] == row['Score']

def test_task_func_with_missing_teams():
    goals = {
        'Team A': 5,
        'Team B': 3,
        'Team D': 8
    }
    penalties = {
        'Team A': 2,
        'Team B': 1,
        'Team C': 3,
        'Team D': 5,
        'Team E': 4
    }

    expected_output = pd.DataFrame({
        'Team': ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'],
        'Score': [3, 2, -3, 3, -4]
    })

    result = task_func(goals, penalties)

    # Check if the DataFrame has the correct columns
    assert list(result.columns) == ['Team', 'Score']

    # Check if the DataFrame has the correct number of rows
    assert len(result) == 5

    # Check if the scores are correctly calculated and clipped
    for i, row in expected_output.iterrows():
        assert result.loc[i, 'Team'] == row['Team']
        assert result.loc[i, 'Score'] == row['Score']

def test_task_func_with_all_zero_scores():
    goals = {
        'Team A': 0,
        'Team B': 0,
        'Team C': 0,
        'Team D': 0,
        'Team E': 0
    }
    penalties = {
        'Team A': 0,
        'Team B': 0,
        'Team C': 0,
        'Team D': 0,
        'Team E': 0
    }

    expected_output = pd.DataFrame({
        'Team': ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'],
        'Score': [0, 0, 0, 0, 0]
    })

    result = task_func(goals, penalties)

    # Check if the DataFrame has the correct columns
    assert list(result.columns) == ['Team', 'Score']

    # Check if the DataFrame has the correct number of rows
    assert len(result) == 5

    # Check if the scores are correctly calculated and clipped
    for i, row in expected_output.iterrows():
        assert result.loc[i, 'Team'] == row['Team']
        assert result.loc[i, 'Score'] == row['Score']

def test_task_func_with_negative_clipping():
    goals = {
        'Team A': -15,
        'Team B': 3,
        'Team C': -2,
        'Team D': 8,
        'Team E': -1
    }
    penalties = {
        'Team A': 2,
        'Team B': 1,
        'Team C': 3,
        'Team D': 5,
        'Team E': 4
    }

    expected_output = pd.DataFrame({
        'Team': ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'],
        'Score': [-10, 2, -5, 3, -5]
    })

    result = task_func(goals, penalties)

    # Check if the DataFrame has the correct columns
    assert list(result.columns) == ['Team', 'Score']

    # Check if the DataFrame has the correct number of rows
    assert len(result) == 5

    # Check if the scores are correctly calculated and clipped
    for i, row in expected_output.iterrows():
        assert result.loc[i, 'Team'] == row['Team']
        assert result.loc[i, 'Score'] == row['Score']

def test_task_func_with_positive_clipping():
    goals = {
        'Team A': 5,
        'Team B': 3,
        'Team C': -2,
        'Team D': 20,
        'Team E': -1
    }
    penalties = {
        'Team A': 2,
        'Team B': 1,
        'Team C': 3,
        'Team D': 5,
        'Team E': 4
    }

    expected_output = pd.DataFrame({
        'Team': ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'],
        'Score': [3, 2, -5, 10, -5]
    })

    result = task_func(goals, penalties)

    # Check if the DataFrame has the correct columns
    assert list(result.columns) == ['Team', 'Score']

    # Check if the DataFrame has the correct number of rows
    assert len(result) == 5

    # Check if the scores are correctly calculated and clipped
    for i, row in expected_output.iterrows():
        assert result.loc[i, 'Team'] == row['Team']
        assert result.loc[i, 'Score'] == row['Score']