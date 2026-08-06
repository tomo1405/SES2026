import pytest
from src_0931 import task_func

def test_task_func():
    word = "python"
    expected_output = ['py', 'yp', 'th', 'ho', 'on', 'nt']
    random.seed(42)  # Set the random seed for reproducibility
    actual_output = task_func(word)
    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_invalid_input():
    word = "123"
    with pytest.raises(ValueError) as excinfo:
        task_func(word)
    assert "Input must only contain letters." in str(excinfo.value), "Invalid input did not raise expected ValueError"