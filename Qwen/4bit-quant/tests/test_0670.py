import math

import pytest
from src_0670 import task_func


def test_task_func():
    # Test with a simple dictionary
    x = {'a': 0, 'b': math.pi, 'c': math.pi/2}
    result = task_func(x)
    assert result == ('a', 'c'), "Test case 1 failed"

    # Test with all values being the same
    x = {'a': 0, 'b': 0, 'c': 0}
    result = task_func(x)
    assert result == ('a', 'b'), "Test case 2 failed"

    # Test with negative values
    x = {'a': -math.pi, 'b': -math.pi/2, 'c': -math.pi/4}
    result = task_func(x)
    assert result == ('a', 'b'), "Test case 3 failed"

    # Test with a single element (should raise an error)
    x = {'a': 0}
    with pytest.raises(ValueError):
        task_func(x)

    # Test with no elements (should raise an error)
    x = {}
    with pytest.raises(ValueError):
        task_func(x)

    # Test with large number of elements
    x = {f'key{i}': i * math.pi / 180 for i in range(360)}
    result = task_func(x)
    assert result == ('key0', 'key180'), "Test case 5 failed"