import pytest
from src_0376 import task_func

def test_task_func():
    # Test case 1: Test if the function returns the expected output for a given input
    input_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_output = <expected output>
    actual_output = task_func(input_list)
    assert actual_output == expected_output

    # Test case 2: Test if the function raises an exception for an invalid input
    invalid_input = "invalid input"
    with pytest.raises(Exception) as excinfo:
        task_func(invalid_input)
    assert "Invalid input type" in str(excinfo.value)

    # Test case 3: Test if the function returns the expected output for a different input
    input_list_2 = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
    expected_output_2 = <expected output 2>
    actual_output_2 = task_func(input_list_2)
    assert actual_output_2 == expected_output_2