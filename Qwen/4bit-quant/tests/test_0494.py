import pytest
from src_0494 import task_func
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import io

def test_task_func_with_valid_input():
    epoch_milliseconds = int(datetime.now().timestamp() * 1000) - 86400000  # 1 day ago
    performance_data, fig = task_func(epoch_milliseconds)
    
    assert isinstance(performance_data, dict)
    assert len(performance_data) == 5  # Default number of teams
    for team, data in performance_data.items():
        assert isinstance(team, str)
        assert isinstance(data, list)
        assert len(data) == 1  # 1 day difference

    buf = io.BytesIO()
    fig.savefig(buf)
    buf.seek(0)
    assert buf.getvalue()  # Check if the figure is saved correctly

def test_task_func_with_invalid_teams_type():
    epoch_milliseconds = int(datetime.now().timestamp() * 1000) - 86400000  # 1 day ago
    with pytest.raises(TypeError):
        task_func(epoch_milliseconds, teams={"Team1", "Team2"})

def test_task_func_with_non_string_team():
    epoch_milliseconds = int(datetime.now().timestamp() * 1000) - 86400000  # 1 day ago
    with pytest.raises(TypeError):
        task_func(epoch_milliseconds, teams=["Team1", 2, "Team3"])

def test_task_func_with_future_timestamp():
    epoch_milliseconds = int((datetime.now() + timedelta(days=1)).timestamp() * 1000)  # 1 day in the future
    with pytest.raises(ValueError):
        task_func(epoch_milliseconds)