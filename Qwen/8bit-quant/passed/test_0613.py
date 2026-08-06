import pytest
from src_0613 import task_func
import numpy as np
import pandas as pd

def test_task_func_no_teams():
    goals = {}
    penalties = {}
    result_df = task_func(goals, penalties)
    assert result_df.empty

def test_task_func_single_team():
    goals = {'Team A': 5}
    penalties = {'Team A': 2}
    result_df = task_func(goals, penalties)
    assert len(result_df) == 1
    assert result_df.iloc[0]['Team'] == 'Team A'
    assert result_df.iloc[0]['Goals'] == 5
    assert result_df.iloc[0]['Penalties'] == 2
    assert 0 <= result_df.iloc[0]['Penalties Cost'] <= 1000  # 2 * max(PENALTIES_COSTS)
    assert result_df.iloc[0]['Performance Score'] == 3

def test_task_func_multiple_teams():
    goals = {'Team A': 5, 'Team B': 3}
    penalties = {'Team A': 2, 'Team B': 4}
    result_df = task_func(goals, penalties)
    assert len(result_df) == 2
    for index, row in result_df.iterrows():
        assert row['Team'] in ['Team A', 'Team B']
        assert row['Goals'] in [5, 3]
        assert row['Penalties'] in [2, 4]
        assert 0 <= row['Penalties Cost'] <= 1000  # max(PENALTIES_COSTS) * max(PENALTIES)
        assert row['Performance Score'] in [3, -1]

def test_task_func_missing_team_in_goals():
    goals = {'Team A': 5}
    penalties = {'Team A': 2, 'Team B': 4}
    result_df = task_func(goals, penalties)
    assert len(result_df) == 2
    for index, row in result_df.iterrows():
        if row['Team'] == 'Team B':
            assert row['Goals'] == 0
            assert row['Penalties'] == 4
            assert 0 <= row['Penalties Cost'] <= 2000  # 4 * max(PENALTIES_COSTS)
            assert row['Performance Score'] == -4

def test_task_func_missing_team_in_penalties():
    goals = {'Team A': 5, 'Team B': 3}
    penalties = {'Team B': 4}
    result_df = task_func(goals, penalties)
    assert len(result_df) == 2
    for index, row in result_df.iterrows():
        if row['Team'] == 'Team A':
            assert row['Goals'] == 5
            assert row['Penalties'] == 0
            assert row['Penalties Cost'] == 0
            assert row['Performance Score'] == 5

def test_task_func_custom_teams_and_penalties_costs():
    goals = {'Custom Team 1': 7, 'Custom Team 2': 2}
    penalties = {'Custom Team 1': 3, 'Custom Team 2': 1}
    custom_teams = ['Custom Team 1', 'Custom Team 2']
    custom_penalties_costs = [150, 250]
    result_df = task_func(goals, penalties, teams=custom_teams, penalties_costs=custom_penalties_costs)
    assert len(result_df) == 2
    for index, row in result_df.iterrows():
        if row['Team'] == 'Custom Team 1':
            assert row['Goals'] == 7
            assert row['Penalties'] == 3
            assert 450 <= row['Penalties Cost'] <= 900  # 3 * max(custom_penalties_costs)
            assert row['Performance Score'] == 4
        elif row['Team'] == 'Custom Team 2':
            assert row['Goals'] == 2
            assert row['Penalties'] == 1
            assert 250 <= row['Penalties Cost'] <= 250  # 1 * max(custom_penalties_costs)
            assert row['Performance Score'] == 1