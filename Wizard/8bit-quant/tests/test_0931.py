python
import random
import string
import pytest

from src_0931 import task_func

def test_task_func():
    # Test valid input
    assert task_func('abc') == ['ab', 'bc']
    assert task_func('abcd') == ['ab', 'bc', 'cd']
    assert task_func('abcde') == ['ab', 'bc', 'cd', 'de']

    # Test invalid input
    with pytest.raises(ValueError):
        task_func('123')

    with pytest.raises(ValueError):
        task_func('a')

    with pytest.raises(ValueError):
        task_func('')

    # Test edge cases
    assert task_func('a') == ['', '']
    assert task_func('') == ['', '', '']