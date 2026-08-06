import os

from src_0732 import task_func


def test_task_func():
    # Call the function with the provided DATA and TARGET
    result_data, result_target = task_func(DATA, TARGET)
    
    # Check if the returned data and target match the original DATA and TARGET
    assert (result_data == DATA).all(), "The returned data does not match the original data"
    assert (result_target == TARGET).all(), "The returned target does not match the original target"
    
    # Check if the file was removed after loading
    assert not os.path.exists(FILE_NAME), "The file was not removed after loading"

    # Check if the function can handle multiple calls without issues
    result_data_2, result_target_2 = task_func(DATA, TARGET)
    assert (result_data_2 == DATA).all(), "The second call returned data does not match the original data"
    assert (result_target_2 == TARGET).all(), "The second call returned target does not match the original target"
    assert not os.path.exists(FILE_NAME), "The file was not removed after the second call"