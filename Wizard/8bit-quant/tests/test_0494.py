python
import pytest
from src_0494 import task_func

def test_task_func():
    with pytest.raises(TypeError):
        task_func(1234567890, teams=123)

    with pytest.raises(TypeError):
        task_func(1234567890, teams=["Team1", "Team2", 3])

    with pytest.raises(ValueError):
        task_func(1234567890000)

    performance_data, fig = task_func(1234567890)
    assert isinstance(performance_data, dict)
    assert isinstance(fig, plt.Figure)
    assert len(performance_data) == 5
    assert all(isinstance(team, str) for team in performance_data.keys())
    assert all(isinstance(performance, list) for performance in performance_data.values())
    assert all(isinstance(day_performance, float) for day_performance in performance_data["Team1"])
    assert all(isinstance(day_performance, float) for day_performance in performance_data["Team2"])
    assert all(isinstance(day_performance, float) for day_performance in performance_data["Team3"])
    assert all(isinstance(day_performance, float) for day_performance in performance_data["Team4"])
    assert all(isinstance(day_performance, float) for day_performance in performance_data["Team5"])
    assert len(performance_data["Team1"]) == 30
    assert len(performance_data["Team2"]) == 30
    assert len(performance_data["Team3"]) == 30
    assert len(performance_data["Team4"]) == 30
    assert len(performance_data["Team5"]) == 30
    assert isinstance(fig.axes[0], plt.Axes)
    assert fig.axes[0].get_xlabel() == "Days since 2009-02-13 09:31:30"
    assert fig.axes[0].get_ylabel() == "Performance"
    assert len(fig.axes[0].lines) == 5
    assert fig.axes[0].lines[0].get_label() == "Team1"
    assert fig.axes[0].lines[1].get_label() == "Team2"
    assert fig.axes[0].lines[2].get_label() == "Team3"
    assert fig.axes[0].lines[3].get_label() == "Team4"
    assert fig.axes[0].lines[4].get_label() == "Team5"
    assert all(isinstance(line.get_xdata(), np.ndarray) for line in fig.axes[0].lines)
    assert all(isinstance(line.get_ydata(), np.ndarray) for line in fig.axes[0].lines)
    assert all(len(line.get_xdata()) == 30 for line in fig.axes[0].lines)
    assert all(len(line.get_ydata()) == 30 for line in fig.axes[0].lines)
    assert all(isinstance(line.get_xdata()[0], float) for line in fig.axes[0].lines)
    assert all(isinstance(line.get_ydata()[0], float) for line in fig.axes[0].lines)