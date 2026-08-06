from datetime import datetime

import matplotlib.pyplot as plt
import pytest
from src_0494 import task_func


def test_task_func_invalid_teams_type():
    with pytest.raises(TypeError):
        task_func(1672531200000, teams="Not a list")

def test_task_func_invalid_teams_elements():
    with pytest.raises(TypeError):
        task_func(1672531200000, teams=[1, 2, 3])

def test_task_func_future_timestamp():
    with pytest.raises(ValueError):
        future_timestamp = int((datetime.now() + timedelta(days=1)).timestamp()) * 1000
        task_func(future_timestamp)

def test_task_func_valid_input():
    epoch_milliseconds = 1672531200000  # Example timestamp for January 1, 2023
    performance_data, fig = task_func(epoch_milliseconds)

    assert isinstance(performance_data, dict)
    assert all(isinstance(team, str) and isinstance(data, list) for team, data in performance_data.items())
    assert all(isinstance(value, float) for team in performance_data for value in performance_data[team])
    assert len(performance_data["Team1"]) == (datetime.now() - datetime.fromtimestamp(epoch_milliseconds / 1000.0)).days

    assert isinstance(fig, plt.Figure)

def test_task_func_with_custom_teams_and_seed():
    epoch_milliseconds = 1672531200000
    custom_teams = ["Alpha", "Beta"]
    custom_seed = 42
    performance_data, fig = task_func(epoch_milliseconds, teams=custom_teams, random_seed=custom_seed)

    assert list(performance_data.keys()) == custom_teams
    assert len(performance_data["Alpha"]) == (datetime.now() - datetime.fromtimestamp(epoch_milliseconds / 1000.0)).days

    assert isinstance(fig, plt.Figure)