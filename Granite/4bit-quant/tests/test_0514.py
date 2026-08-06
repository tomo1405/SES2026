import pytest
from src_0514 import task_func


def test_task_func_valid_column():
    column = "Steps"
    data = [
        ["2022-01-01", 100, 200, 50],
        ["2022-01-02", 150, 250, 75],
        ["2022-01-03", 200, 300, 100],
    ]
    expected_result = {
        "sum": 550,
        "mean": 183.33333333333334,
        "min": 100,
        "max": 200,
    }
    expected_ax_title = "Line Chart of Steps"
    result, ax = task_func(column, data)
    assert result == expected_result
    assert ax.get_title() == expected_ax_title

def test_task_func_invalid_column():
    column = "Invalid Column"
    data = [
        ["2022-01-01", 100, 200, 50],
        ["2022-01-02", 150, 250, 75],
        ["2022-01-03", 200, 300, 100],
    ]
    with pytest.raises(KeyError) as exc_info:
        task_func(column, data)
    assert "Invalid Column is not a valid column. Choose from ['Date', 'Steps', 'Calories Burned', 'Distance Walked']." in str(exc_info.value)

def test_task_func_no_data():
    column = "Steps"
    data = []
    with pytest.raises(ValueError) as exc_info:
        task_func(column, data)
    assert "No data to plot." in str(exc_info.value)

def test_task_func_negative_values():
    column = "Steps"
    data = [
        ["2022-01-01", -100, 200, 50],
        ["2022-01-02", 150, 250, 75],
        ["2022-01-03", 200, 300, 100],
    ]
    with pytest.raises(ValueError) as exc_info:
        task_func(column, data)
    assert "Numeric values for steps, calories burned, and distance walked must be non-negative." in str(exc_info.value)