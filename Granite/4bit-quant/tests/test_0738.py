import pytest
import numpy as np
import math

from src_0738 import task_func

def test_task_func():
    L = [1, 2, 3, 4, 5]
    expected_output = 3
    actual_output = task_func(L)
    assert actual_output == expected_output, "Test case 1 failed"

    L = [[1, 2], [3, 4], [5, 6]]
    expected_output = 3.5
    actual_output = task_func(L)
    assert actual_output == expected_output, "Test case 2 failed"

    L = []
    with pytest.raises(ValueError):
        task_func(L)

    L = [1, "a", 2, "b", 3]
    expected_output = 2.5
    actual_output = task_func(L)
    assert actual_output == expected_output, "Test case 4 failed"