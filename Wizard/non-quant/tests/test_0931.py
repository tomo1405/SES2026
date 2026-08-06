python
import random
import string
import pytest

from src_0931 import task_func

def test_task_func():
    # Test case 1
    word = 'abc'
    expected_result = ['ab', 'ac', 'bc']
    assert task_func(word) == expected_result
    
    # Test case 2
    word = 'ab'
    expected_result = ['', '']
    assert task_func(word) == expected_result
    
    # Test case 3
    word = '123'
    with pytest.raises(ValueError):
        task_func(word)
    
    # Test case 4
    word = 'a'
    expected_result = ['', '']
    assert task_func(word) == expected_result
    
    # Test case 5
    word = 'ab'
    expected_result = ['ab', 'ab', 'ab']
    assert task_func(word) == expected_result
    
    # Test case 6
    word = 'abc'
    expected_result = ['ab', 'ac', 'bc']
    assert task_func(word) == expected_result
    
    # Test case 7
    word = 'abcd'
    expected_result = ['ab', 'ac', 'ad']
    assert task_func(word) == expected_result
    
    # Test case 8
    word = 'abcde'
    expected_result = ['ab', 'ac', 'ad']
    assert task_func(word) == expected_result
    
    # Test case 9
    word = 'abcdef'
    expected_result = ['ab', 'ac', 'ad']
    assert task_func(word) == expected_result
    
    # Test case 10
    word = 'abcdefgh'
    expected_result = ['ab', 'ac', 'ad']
    assert task_func(word) == expected_result