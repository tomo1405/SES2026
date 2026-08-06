import math

import pytest
from src_0670 import task_func


def test_task_func():
    # Test case 1: Simple dictionary with positive values
    x = {0: 0, 1: math.pi/2, 2: math.pi}
    assert task_func(x) == (0, 1)

    # Test case 2: Dictionary with negative values
    x = {0: -math.pi, 1: -math.pi/2, 2: -math.pi/4}
    assert task_func(x) == (0, 2)

    # Test case 3: Dictionary with mixed values
    x = {0: math.pi/4, 1: math.pi/3, 2: math.pi/6}
    assert task_func(x) == (0, 2)

    # Test case 4: Dictionary with all zero values
    x = {0: 0, 1: 0, 2: 0}
    assert task_func(x) == (0, 1)

    # Test case 5: Single element dictionary (should raise ValueError)
    with pytest.raises(ValueError):
        x = {0: 0}
        task_func(x)

    # Test case 6: Empty dictionary (should raise ValueError)
    with pytest.raises(ValueError):
        x = {}
        task_func(x)