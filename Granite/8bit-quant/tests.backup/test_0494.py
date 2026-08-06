import pytest
from src_0494 import task_func

def test_task_func_valid_input():
    teams = ["Team1", "Team2", "Team3", "Team4", "Team5"]
    epoch_milliseconds = 1631840400000
    random_seed = 0
    expected_output = ({'Team1': [0.5783443414440431, 0.2847782506331641], 'Team2': [0.12345678901234568, 0.9876543210987654], 'Team3': [0.3456789012345679, 0.6543210987654321], 'Team4': [0.7890123456789012, 0.5432109876543211], 'Team5': [0.9012345678901234, 0.8765432109876543]}, <matplotlib.figure.Figure object at 0x7f12e9111d50>)
    actual_output = task_func(epoch_milliseconds, teams, random_seed)
    assert actual_output == expected_output

def test_task_func_invalid_teams():
    teams = ["Team1", "Team2", 3, "Team4", "Team5"]
    epoch_milliseconds = 1631840400000
    random_seed = 0
    with pytest.raises(TypeError):
        task_func(epoch_milliseconds, teams, random_seed)

def test_task_func_future_timestamp():
    teams = ["Team1", "Team2", "Team3", "Team4", "Team5"]
    epoch_milliseconds = 1631840400000000
    random_seed = 0
    with pytest.raises(ValueError):
        task_func(epoch_milliseconds, teams, random_seed)