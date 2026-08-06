import pytest
from src_0618 import task_func
from random import seed
import pandas as pd

def test_task_func_default_teams():
    seed(42)  # Ensure reproducibility
    df = task_func(goals=5, penalties=3)
    expected_teams = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
    assert list(df['Team']) == expected_teams

def test_task_func_custom_teams():
    seed(42)  # Ensure reproducibility
    custom_teams = ['Team X', 'Team Y']
    df = task_func(goals=5, penalties=3, teams=custom_teams)
    assert list(df['Team']) == custom_teams

def test_task_func_no_teams():
    seed(42)  # Ensure reproducibility
    df = task_func(goals=5, penalties=3, teams=[])
    assert df.empty

def test_task_func_result_format():
    seed(42)  # Ensure reproducibility
    df = task_func(goals=5, penalties=3)
    for result in df['Match Result']:
        assert re.match(r'\(\d+ goals, \$\d+\)', result)

def test_task_func_goals_and_penalty_cost_columns():
    seed(42)  # Ensure reproducibility
    df = task_func(goals=5, penalties=3)
    assert 'Goals' in df.columns
    assert 'Penalty Cost' in df.columns

def test_task_func_goals_and_penalty_cost_values():
    seed(42)  # Ensure reproducibility
    df = task_func(goals=5, penalties=3)
    for index, row in df.iterrows():
        goals_match = re.search(r'\((\d+) goals', row['Match Result'])
        penalty_cost_match = re.search(r'\$(\d+)', row['Match Result'])
        assert int(goals_match.group(1)) == row['Goals']
        assert int(penalty_cost_match.group(1)) == row['Penalty Cost']

def test_task_func_with_rng_seed():
    seed(42)  # Ensure reproducibility
    df1 = task_func(goals=5, penalties=3, rng_seed=42)
    df2 = task_func(goals=5, penalties=3, rng_seed=42)
    assert df1.equals(df2)

def test_task_func_without_rng_seed():
    df1 = task_func(goals=5, penalties=3)
    df2 = task_func(goals=5, penalties=3)
    assert not df1.equals(df2)