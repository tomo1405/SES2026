import pytest
from src_0668 import task_func

def test_task_func():
    x = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    n = 3
    expected_output = [1, 2, 3]

    actual_output = task_func(x, n)

    assert actual_output == expected_output, "Output does not match expected output"