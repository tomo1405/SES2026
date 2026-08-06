import pytest
from src_0494 import task_func

def test_task_func():
    # Test case 1: Test with valid input
    epoch_milliseconds = 1631840400000
    teams = ["Team1", "Team2", "Team3", "Team4", "Team5"]
    random_seed = 0
    expected_output = ({'Team1': [0.5789473684210527, 0.5789473684210527, 0.5789473684210527], 'Team2': [0.5789473684210527, 0.5789473684210527, 0.5789473684210527], 'Team3': [0.5789473684210527, 0.5789473684210527, 0.5789473684210527], 'Team4': [0.5789473684210527, 0.5789473684210527, 0.5789473684210527], 'Team5': [0.5789473684210527, 0.5789473684210527, 0.5789473684210527]}, <matplotlib.figure.Figure object at 0x7f225e9b7e10>)
    actual_output = task_func(epoch_milliseconds, teams, random_seed)
    assert actual_output == expected_output

    # Test case 2: Test with invalid input (teams is not a list)
    epoch_milliseconds = 1631840400000
    teams = "Invalid input"
    random_seed = 0
    with pytest.raises(TypeError):
        task_func(epoch_milliseconds, teams, random_seed)

    # Test case 3: Test with invalid input (teams contains non-string elements)
    epoch_milliseconds = 1631840400000
    teams = ["Team1", "Team2", 3]
    random_seed = 0
    with pytest.raises(TypeError):
        task_func(epoch_milliseconds, teams, random_seed)

    # Test case 4: Test with invalid input (epoch_milliseconds is in the future)
    epoch_milliseconds = 1631840400001
    teams = ["Team1", "Team2", "Team3", "Team4", "Team5"]
    random_seed = 0
    with pytest.raises(ValueError):
        task_func(epoch_milliseconds, teams, random_seed)