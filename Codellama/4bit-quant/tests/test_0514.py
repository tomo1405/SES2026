import pytest
from src_0514 import task_func

def test_task_func():
    # Test with valid column and data
    column = "Steps"
    data = [
        ["2022-01-01", 1000, 200, 3],
        ["2022-01-02", 1200, 250, 4],
        ["2022-01-03", 1400, 300, 5],
    ]
    result, ax = task_func(column, data)
    assert result == {
        "sum": 3700,
        "mean": 1200,
        "min": 1000,
        "max": 1400,
    }
    assert ax.get_ylabel() == "Steps"
    assert ax.get_title() == "Line Chart of Steps"

    # Test with invalid column
    with pytest.raises(KeyError):
        task_func("Invalid Column", data)

    # Test with no data
    with pytest.raises(ValueError):
        task_func(column, [])

    # Test with negative values
    data = [
        ["2022-01-01", -1000, 200, 3],
        ["2022-01-02", -1200, 250, 4],
        ["2022-01-03", -1400, 300, 5],
    ]
    with pytest.raises(ValueError):
        task_func(column, data)