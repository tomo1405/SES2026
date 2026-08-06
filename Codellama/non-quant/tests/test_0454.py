import pytest
from src_0454 import task_func

def test_task_func():
    # Test case 1: n = 1, pattern = 'a'
    assert task_func(1, 'a') == 'a'

    # Test case 2: n = 2, pattern = 'ab'
    assert task_func(2, 'ab') == 'ab'

    # Test case 3: n = 3, pattern = 'abc'
    assert task_func(3, 'abc') == 'abc'

    # Test case 4: n = 4, pattern = 'abcd'
    assert task_func(4, 'abcd') == 'abcd'

    # Test case 5: n = 5, pattern = 'abcde'
    assert task_func(5, 'abcde') == 'abcde'

    # Test case 6: n = 6, pattern = 'abcdef'
    assert task_func(6, 'abcdef') == 'abcdef'

    # Test case 7: n = 7, pattern = 'abcdefg'
    assert task_func(7, 'abcdefg') == 'abcdefg'

    # Test case 8: n = 8, pattern = 'abcdefgh'
    assert task_func(8, 'abcdefgh') == 'abcdefgh'

    # Test case 9: n = 9, pattern = 'abcdefghi'
    assert task_func(9, 'abcdefghi') == 'abcdefghi'

    # Test case 10: n = 10, pattern = 'abcdefghij'
    assert task_func(10, 'abcdefghij') == 'abcdefghij'