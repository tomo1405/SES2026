import pytest
from src_0329 import task_func

def test_task_func():
    # Test with default number of teams
    expected_ranking = {
        "Team 1": -10,
        "Team 2": -20,
        "Team 3": -30,
        "Team 4": -40,
        "Team 5": -50
    }
    assert task_func() == expected_ranking

    # Test with custom number of teams
    expected_ranking = {
        "Team 1": -10,
        "Team 2": -20,
        "Team 3": -30,
        "Team 4": -40,
        "Team 5": -50,
        "Team 6": -60,
        "Team 7": -70,
        "Team 8": -80,
        "Team 9": -90,
        "Team 10": -100
    }
    assert task_func(10) == expected_ranking