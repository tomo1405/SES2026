import pytest
from src_0613 import task_func
import numpy as np
import pandas as pd

def test_task_func_no_teams():
    goals = {}
    penalties = {}
    result = task_func(goals, penalties)
    assert result.empty

def test_task_func_single_team():
    goals = {'Team A': 5}
    penalties = {'Team A': 2}
    result = task_func(goals, penalties)
    assert len(result) == 1
    row = result.iloc[0]
    assert row['Team'] == 'Team A'
    assert row['Goals'] == 5
    assert row['Penalties'] == 2
    assert row['Performance Score'] >= 0
    assert row['Penalties Cost'] >= 0 and row['Penalties Cost'] <= 1000

def test_task_func_multiple_teams():
    goals = {'Team A': 5, 'Team B': 3}
    penalties = {'Team A': 2, 'Team B': 4}
    result = task_func(goals, penalties)
    assert len(result) == 2
    for index, row in result.iterrows():
        assert row['Team'] in ['Team A', 'Team B']
        assert row['Goals'] in [5, 3]
        assert row['Penalties'] in [2, 4]
        assert row['Performance Score'] >= 0
        assert row['Penalties Cost'] >= 0 and row['Penalties Cost'] <= 1000

def test_task_func_no_penalties():
    goals = {'Team A': 5}
    penalties = {'Team A': 0}
    result = task_func(goals, penalties)
    row = result.iloc[0]
    assert row['Penalties Cost'] == 0
    assert row['Performance Score'] == 5

def test_task_func_all_teams():
    goals = {team: i for i, team in enumerate(TEAMS)}
    penalties = {team: i for i, team in enumerate(TEAMS)}
    result = task_func(goals, penalties)
    assert len(result) == len(TEAMS)
    for index, row in result.iterrows():
        assert row['Team'] in TEAMS
        assert row['Goals'] == TEAMS.index(row['Team'])
        assert row['Penalties'] == TEAMS.index(row['Team'])
        assert row['Performance Score'] >= 0
        assert row['Penalties Cost'] >= 0 and row['Penalties Cost'] <= 1000

def test_task_func_custom_teams_and_costs():
    custom_teams = ['Team X', 'Team Y']
    custom_penalties_costs = [10, 20]
    goals = {team: 5 for team in custom_teams}
    penalties = {team: 2 for team in custom_teams}
    result = task_func(goals, penalties, teams=custom_teams, penalties_costs=custom_penalties_costs)
    assert len(result) == len(custom_teams)
    for index, row in result.iterrows():
        assert row['Team'] in custom_teams
        assert row['Goals'] == 5
        assert row['Penalties'] == 2
        assert row['Performance Score'] == 3
        assert row['Penalties Cost'] >= 20 and row['Penalties Cost'] <= 40

def test_task_func_random_penalties_cost():
    goals = {'Team A': 5}
    penalties = {'Team A': 2}
    result1 = task_func(goals, penalties)
    result2 = task_func(goals, penalties)
    row1 = result1.iloc[0]
    row2 = result2.iloc[0]
    assert row1['Penalties Cost'] != row2['Penalties Cost']