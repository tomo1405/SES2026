import pytest
from src_0494 import task_func

def test_task_func():
    epoch_milliseconds = 1647225600000
    teams = ["Team1", "Team2", "Team3", "Team4", "Team5"]
    random_seed = 0

    performance_data, fig = task_func(epoch_milliseconds, teams, random_seed)

    assert isinstance(performance_data, dict)
    assert all(isinstance(team, str) for team in teams)
    assert all(isinstance(performance, float) for performance in performance_data.values())
    assert all(performance >= 0.1 for performance in performance_data.values())
    assert all(performance <= 1 for performance in performance_data.values())
    assert fig is not None
    assert isinstance(fig, matplotlib.figure.Figure)

def test_task_func_invalid_teams():
    epoch_milliseconds = 1647225600000
    teams = ["Team1", "Team2", "Team3", "Team4", "Team5"]
    random_seed = 0

    with pytest.raises(TypeError):
        task_func(epoch_milliseconds, teams, random_seed)

def test_task_func_invalid_epoch_timestamp():
    epoch_milliseconds = 1647225600000
    teams = ["Team1", "Team2", "Team3", "Team4", "Team5"]
    random_seed = 0

    with pytest.raises(ValueError):
        task_func(epoch_milliseconds, teams, random_seed)