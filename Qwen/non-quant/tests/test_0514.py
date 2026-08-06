import matplotlib.pyplot as plt
import pytest
from src_0514 import task_func


def test_task_func_valid_column():
    data = [
        ["2023-01-01", 1000, 50, 0.5],
        ["2023-01-02", 2000, 100, 1.0],
        ["2023-01-03", 1500, 75, 0.75]
    ]
    result, ax = task_func("Steps", data)
    assert result == {"sum": 4500, "mean": 1500.0, "min": 1000, "max": 2000}
    assert isinstance(ax, plt.Axes)

def test_task_func_invalid_column():
    data = [
        ["2023-01-01", 1000, 50, 0.5],
        ["2023-01-02", 2000, 100, 1.0],
        ["2023-01-03", 1500, 75, 0.75]
    ]
    with pytest.raises(KeyError) as excinfo:
        task_func("InvalidColumn", data)
    assert str(excinfo.value) == "'InvalidColumn' is not a valid column. Choose from ['Date', 'Steps', 'Calories Burned', 'Distance Walked']."


def test_task_func_no_data():
    data = []
    with pytest.raises(ValueError) as excinfo:
        task_func("Steps", data)
    assert str(excinfo.value) == "No data to plot."

def test_task_func_negative_values():
    data = [
        ["2023-01-01", -1000, 50, 0.5],
        ["2023-01-02", 2000, 100, 1.0],
        ["2023-01-03", 1500, 75, 0.75]
    ]
    with pytest.raises(ValueError) as excinfo:
        task_func("Steps", data)
    assert str(excinfo.value) == "Numeric values for steps, calories burned, and distance walked must be non-negative."

def test_task_func_calories_burned():
    data = [
        ["2023-01-01", 1000, 50, 0.5],
        ["2023-01-02", 2000, 100, 1.0],
        ["2023-01-03", 1500, 75, 0.75]
    ]
    result, ax = task_func("Calories Burned", data)
    assert result == {"sum": 225, "mean": 75.0, "min": 50, "max": 100}
    assert isinstance(ax, plt.Axes)

def test_task_func_distance_walked():
    data = [
        ["2023-01-01", 1000, 50, 0.5],
        ["2023-01-02", 2000, 100, 1.0],
        ["2023-01-03", 1500, 75, 0.75]
    ]
    result, ax = task_func("Distance Walked", data)
    assert result == {"sum": 2.25, "mean": 0.75, "min": 0.5, "max": 1.0}
    assert isinstance(ax, plt.Axes)