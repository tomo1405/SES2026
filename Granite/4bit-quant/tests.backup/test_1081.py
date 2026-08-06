import pytest
from src_1081 import task_func

def test_task_func():
    # Test case 1: Test with valid input
    area_string = "2,000"
    expected_output = 200
    actual_output = task_func(area_string)
    assert actual_output == expected_output, "Test case 1 failed"

    # Test case 2: Test with invalid input
    area_string = "invalid"
    with pytest.raises(ValueError):
        task_func(area_string)