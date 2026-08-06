python
import pytest
from src_0508 import task_func

def test_task_func():
    # Test valid input
    data = [
        ["2021-01-01", 10.0, 20.0, 5.0, 15.0, 100],
        ["2021-01-02", 15.0, 25.0, 10.0, 20.0, 200],
        ["2021-01-03", 20.0, 30.0, 15.0, 25.0, 300],
    ]
    result = task_func("Close", data)
    assert result["sum"] == 65.0
    assert result["mean"] == 15.0
    assert result["min"] == 5.0
    assert result["max"] == 25.0

    # Test invalid column name
    with pytest.raises(ValueError):
        task_func("Invalid", data)

    # Test invalid data format
    with pytest.raises(ValueError):
        task_func("Close", [1, 2, 3])

    # Test empty data
    with pytest.raises(ValueError):
        task_func("Close", [])