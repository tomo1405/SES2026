import pytest
from src_0454 import task_func

def test_task_func():
    # Test case 1: n = 1, pattern = '^[a-zA-Z]+$'
    n = 1
    pattern = '^[a-zA-Z]+$'
    result = task_func(n, pattern)
    assert result == 'a'

    # Test case 2: n = 2, pattern = '^[a-zA-Z]+$'
    n = 2
    pattern = '^[a-zA-Z]+$'
    result = task_func(n, pattern)
    assert result == 'ab'

    # Test case 3: n = 3, pattern = '^[a-zA-Z]+$'
    n = 3
    pattern = '^[a-zA-Z]+$'
    result = task_func(n, pattern)
    assert result == 'abc'

    # Test case 4: n = 1, pattern = '^[a-zA-Z0-9]+$'
    n = 1
    pattern = '^[a-zA-Z0-9]+$'
    result = task_func(n, pattern)
    assert result == 'a'

    # Test case 5: n = 2, pattern = '^[a-zA-Z0-9]+$'
    n = 2
    pattern = '^[a-zA-Z0-9]+$'
    result = task_func(n, pattern)
    assert result == 'ab'

    # Test case 6: n = 3, pattern = '^[a-zA-Z0-9]+$'
    n = 3
    pattern = '^[a-zA-Z0-9]+$'
    result = task_func(n, pattern)
    assert result == 'abc'

    # Test case 7: n = 1, pattern = '^[a-zA-Z0-9_]+$'
    n = 1
    pattern = '^[a-zA-Z0-9_]+$'
    result = task_func(n, pattern)
    assert result == 'a'

    # Test case 8: n = 2, pattern = '^[a-zA-Z0-9_]+$'
    n = 2
    pattern = '^[a-zA-Z0-9_]+$'
    result = task_func(n, pattern)
    assert result == 'ab'

    # Test case 9: n = 3, pattern = '^[a-zA-Z0-9_]+$'
    n = 3
    pattern = '^[a-zA-Z0-9_]+$'
    result = task_func(n, pattern)
    assert result == 'abc'

    # Test case 10: n = 1, pattern = '^[a-zA-Z0-9_-]+$'
    n = 1
    pattern = '^[a-zA-Z0-9_-]+$'
    result = task_func(n, pattern)
    assert result == 'a'

    # Test case 11: n = 2, pattern = '^[a-zA-Z0-9_-]+$'
    n = 2
    pattern = '^[a-zA-Z0-9_-]+$'
    result = task_func(n, pattern)
    assert result == 'ab'

    # Test case 12: n = 3, pattern = '^[a-zA-Z0-9_-]+$'
    n = 3
    pattern = '^[a-zA-Z0-9_-]+$'
    result = task_func(n, pattern)
    assert result == 'abc'