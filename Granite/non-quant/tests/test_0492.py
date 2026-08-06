import pytest
from src_0492 import task_func

def test_task_func():
    # Test case 1: Test with valid input
    epoch_milliseconds = 1631840000000
    seed = 42
    sales_data, ax = task_func(epoch_milliseconds, seed)
    assert isinstance(sales_data, dict)
    assert isinstance(ax, object)

    # Test case 2: Test with invalid input (negative epoch_milliseconds)
    with pytest.raises(ValueError) as excinfo:
        task_func(-1, seed)
    assert "Start time cannot be negative." in str(excinfo.value)

    # Test case 3: Test with invalid input (start date after current time)
    with pytest.raises(ValueError) as excinfo:
        task_func(1631840000000, seed)
    assert "Start date must be before current time." in str(excinfo.value)