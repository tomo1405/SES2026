import pytest
from src_0625 import task_func

def test_task_func():
    # Test case 1: Test with a list of two-dimensional data points
    L = [[1, 2], [3, 4], [5, 6]]
    expected_output = ([[-2.44948974, -0.81110711], [ 0.44948974, -0.81110711], [ 2.44948974,  0.81110711]], <matplotlib.axes._subplots.AxesSubplot object at 0x7f225e91c1d0>)
    actual_output = task_func(L)
    assert actual_output == expected_output, "Test case 1 failed"

    # Test case 2: Test with a list of three-dimensional data points
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_output = ([[ 2.23606798, -0.70710678], [ 0.        ,  0.        ], [-2.23606798,  0.70710678]], <matplotlib.axes._subplots.AxesSubplot object at 0x7f225e91c210>)
    actual_output = task_func(L)
    assert actual_output == expected_output, "Test case 2 failed"

if __name__ == "__main__":
    pytest.main()