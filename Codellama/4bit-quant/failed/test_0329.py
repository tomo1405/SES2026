import pytest
from src_0329 import task_func

def test_task_func():
    # Test with default number of teams
    expected_output = {"Team 1": -10, "Team 2": -20, "Team 3": -30, "Team 4": -40, "Team 5": -50}
    assert task_func() == expected_output

    # Test with custom number of teams
    expected_output = {"Team 1": -10, "Team 2": -20, "Team 3": -30, "Team 4": -40, "Team 5": -50, "Team 6": -60}
    assert task_func(6) == expected_output

    # Test with invalid number of teams
    with pytest.raises(ValueError):
        task_func(-1)