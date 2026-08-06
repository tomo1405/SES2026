import pytest
from src_0949 import task_func

def test_task_func():
    # Test case 1: Default input values
    expected_output = [[0.52104922, 0.49467915],
                       [0.4865454 , 0.4865454 ],
                       [0.49467915, 0.52104922]]
    actual_output = task_func()
    assert pytest.approx(expected_output) == actual_output

    # Test case 2: Custom input values
    expected_output = [[0.29193404, 0.29193404],
                       [0.29193404, 0.29193404],
                       [0.29193404, 0.29193404]]
    actual_output = task_func(rows=3, columns=2, seed=42)
    assert pytest.approx(expected_output) == actual_output