import pytest
from src_0621 import task_func

def test_task_func():
    # Test case 1: Test with a valid input
    input_list = [(2, 3), (4, 5)]
    expected_output_shape = (8, 15)
    actual_output = task_func(input_list)
    assert actual_output.shape == expected_output_shape

    # Test case 2: Test with an invalid input
    input_list = [(10, 20), (30, 40), (50, 60)]
    with pytest.raises(ValueError):
        task_func(input_list)