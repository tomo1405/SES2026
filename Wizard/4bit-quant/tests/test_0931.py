python
import random
import string
import pytest

from src_0931 import task_func

def test_task_func():
    # Test case 1: Valid input
    word = 'abc'
    expected_output = ['ab', 'ac', 'bc']
    assert task_func(word) == expected_output

    # Test case 2: Input contains non-letter characters
    word = '123'
    with pytest.raises(ValueError):
        task_func(word)

    # Test case 3: Input is too short
    word = 'a'
    expected_output = ['', '', '']
    assert task_func(word) == expected_output