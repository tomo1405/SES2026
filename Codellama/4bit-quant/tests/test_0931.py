import pytest
from src_0931 import task_func

def test_task_func():
    # Test that the function raises a ValueError when the input contains non-letters
    with pytest.raises(ValueError):
        task_func("abc1")

    # Test that the function returns an empty list when the input is an empty string
    assert task_func("") == []

    # Test that the function returns a list of pairs when the input is a string
    assert task_func("abc") == [('a', 'b'), ('b', 'c')]

    # Test that the function returns a list of pairs when the input is a string with multiple letters
    assert task_func("abcd") == [('a', 'b'), ('b', 'c'), ('c', 'd')]

    # Test that the function returns a list of pairs when the input is a string with multiple letters and spaces
    assert task_func("ab cd") == [('a', 'b'), ('b', 'c'), ('c', 'd')]

    # Test that the function returns a list of pairs when the input is a string with multiple letters and punctuation
    assert task_func("ab,cd") == [('a', 'b'), ('b', 'c'), ('c', 'd')]

    # Test that the function returns a list of pairs when the input is a string with multiple letters and numbers
    assert task_func("ab12") == [('a', 'b'), ('b', '1'), ('1', '2')]

    # Test that the function returns a list of pairs when the input is a string with multiple letters and special characters
    assert task_func("ab!@#") == [('a', 'b'), ('b', '!'), ('!', '@'), ('@', '#')]