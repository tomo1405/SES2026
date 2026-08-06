import pytest
from src_0494 import task_func

def test_task_func_type_error():
    with pytest.raises(TypeError):
        task_func(1234567890, teams=["Team1", "Team2", "Team3", "Team4", "Team5"], random_seed=0)

def test_task_func_value_error():
    with pytest.raises(ValueError):
        task_func(1234567890, teams=["Team1", "Team2", "Team3", "Team4", "Team5"], random_seed=0)

def test_task_func_valid_input():
    performance_data, fig = task_func(1234567890, teams=["Team1", "Team2", "Team3", "Team4", "Team5"], random_seed=0)
    assert isinstance(performance_data, dict)
    assert isinstance(fig, matplotlib.figure.Figure)