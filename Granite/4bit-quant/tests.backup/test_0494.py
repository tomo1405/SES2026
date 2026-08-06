import pytest
from src_0494 import task_func

def test_task_func_valid_input():
    """
    Test valid input to task_func
    """
    teams = ["Team1", "Team2", "Team3", "Team4", "Team5"]
    epoch_milliseconds = 1640995200000
    random_seed = 0
    expected_output = ({'Team1': [0.6234132215420875, 0.234132215420875], 'Team2': [0.1234132215420875, 0.534132215420875], 'Team3': [0.3234132215420875, 0.734132215420875], 'Team4': [0.9234132215420875, 0.834132215420875], 'Team5': [0.4234132215420875, 0.934132215420875]}, <matplotlib.figure.Figure object at 0x7f225e911e10>)
    output = task_func(epoch_milliseconds, teams, random_seed)
    assert output == expected_output

def test_task_func_invalid_teams():
    """
    Test invalid teams input to task_func
    """
    teams = "Invalid input"
    epoch_milliseconds = 1640995200000
    random_seed = 0
    with pytest.raises(TypeError):
        task_func(epoch_milliseconds, teams, random_seed)

def test_task_func_invalid_timestamp():
    """
    Test invalid timestamp input to task_func
    """
    teams = ["Team1", "Team2", "Team3", "Team4", "Team5"]
    epoch_milliseconds = 1000000000000
    random_seed = 0
    with pytest.raises(ValueError):
        task_func(epoch_milliseconds, teams, random_seed)