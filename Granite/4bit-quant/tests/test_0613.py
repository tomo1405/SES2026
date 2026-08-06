import pytest
from src_0613 import task_func

# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTIES_COSTS = [100, 200, 300, 400, 500]
GOALS = {'Team A': 3, 'Team B': 2, 'Team C': 1}
PENALTIES = {'Team A': 2, 'Team B': 1, 'Team C': 3}

def test_task_func():
    goals = GOALS
    penalties =PENALTIES
    report_df = task_func(goals, penalties)
    assert report_df.shape == (len(TEAMS), 5)
    assert report_df['Team'].tolist() == list(TEAMS)
    assert report_df['Goals'].tolist() == [goals.get(team, 0) for team in TEAMS]
    assert report_df['Penalties'].tolist() == [penalties.get(team, 0) for team in TEAMS]
    assert report_df['Penalties Cost'].tolist() == [penalties.get(team, 0) * choice(PENALTIES_COSTS) for team in TEAMS]
    assert report_df['Performance Score'].tolist() == [np.max([0, goals.get(team, 0) - penalties.get(team, 0)]) for team in TEAMS]

def test_task_func_with_empty_goals_and_penalties():
    goals = {}
    penalties = {}
    report_df = task_func(goals, penalties)
    assert report_df.shape == (len(TEAMS), 5)
    assert report_df['Team'].tolist() == list(TEAMS)
    assert report_df['Goals'].tolist() == [goals.get(team, 0) for team in TEAMS]
    assert report_df['Penalties'].tolist() == [penalties.get(team, 0) for team in TEAMS]
    assert report_df['Penalties Cost'].tolist() == [penalties.get(team, 0) * choice(PENALTIES_COSTS) for team in TEAMS]
    assert report_df['Performance Score'].tolist() == [np.max([0, goals.get(team, 0) - penalties.get(team, 0)]) for team in TEAMS]

def test_task_func_with_invalid_goals_and_penalties():
    with pytest.raises(ValueError):
        task_func('invalid_goals', 'invalid_penalties')