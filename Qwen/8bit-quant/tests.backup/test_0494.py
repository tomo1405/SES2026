import pytest
from src_0494 import task_func
from datetime import datetime, timedelta
import random
import matplotlib.pyplot as plt

def test_task_func_with_default_teams_and_random_seed():
    epoch_milliseconds = int((datetime.now() - timedelta(days=5)).timestamp()) * 1000
    performance_data, fig = task_func(epoch_milliseconds, random_seed=42)
    
    assert isinstance(performance_data, dict)
    assert len(performance_data) == 5
    for team, data in performance_data.items():
        assert team in ["Team1", "Team2", "Team3", "Team4", "Team5"]
        assert len(data) == 5
        assert all(isinstance(d, float) for d in data)
        assert all(0.1 <= d <= 1.0 for d in data)
    
    assert isinstance(fig, plt.Figure)

def test_task_func_with_custom_teams():
    epoch_milliseconds = int((datetime.now() - timedelta(days=3)).timestamp()) * 1000
    custom_teams = ["Alpha", "Beta", "Gamma"]
    performance_data, fig = task_func(epoch_milliseconds, teams=custom_teams, random_seed=42)
    
    assert isinstance(performance_data, dict)
    assert len(performance_data) == 3
    for team, data in performance_data.items():
        assert team in custom_teams
        assert len(data) == 3
        assert all(isinstance(d, float) for d in data)
        assert all(0.1 <= d <= 1.0 for d in data)
    
    assert isinstance(fig, plt.Figure)

def test_task_func_with_future_timestamp():
    epoch_milliseconds = int((datetime.now() + timedelta(days=1)).timestamp()) * 1000
    with pytest.raises(ValueError):
        task_func(epoch_milliseconds)

def test_task_func_with_invalid_teams_type():
    epoch_milliseconds = int((datetime.now() - timedelta(days=5)).timestamp()) * 1000
    with pytest.raises(TypeError):
        task_func(epoch_milliseconds, teams="Not a list")

def test_task_func_with_invalid_teams_elements():
    epoch_milliseconds = int((datetime.now() - timedelta(days=5)).timestamp()) * 1000
    with pytest.raises(TypeError):
        task_func(epoch_milliseconds, teams=["Team1", 2, "Team3"])