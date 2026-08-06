import pytest
from src_0329 import task_func

def test_task_func():
    assert task_func(number_teams=5) == {
        "Team 5": -50,
        "Team 4": -40,
        "Team 3": -30,
        "Team 2": -20,
        "Team 1": -10,
    }
    assert task_func(number_teams=3) == {
        "Team 3": -30,
        "Team 2": -20,
        "Team 1": -10,
    }
    with pytest.raises(ValueError):
        task_func(number_teams=0)
    with pytest.raises(ValueError):
        task_func(number_teams=-1)