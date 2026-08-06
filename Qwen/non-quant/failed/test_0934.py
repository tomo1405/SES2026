import pytest
from src_0934 import task_func

def test_task_func():
    # Test case 1: Simple word
    result = task_func("apple")
    expected_tuples = [('a', 1), ('p', 16), ('p', 16), ('l', 12), ('e', 5)]
    expected_split = ['apple']
    assert result[0] == expected_tuples
    assert result[1] == expected_split

    # Test case 2: Word with multiple splits
    result = task_func("unitedstates")
    expected_tuples = [('u', 21), ('n', 14), ('i', 9), ('t', 20), ('e', 5), ('d', 4), ('s', 19), ('t', 20), ('a', 1), ('t', 20), ('e', 5), ('s', 19)]
    expected_split = ['united', 'states']
    assert result[0] == expected_tuples
    assert result[1] == expected_split

    # Test case 3: Single letter
    result = task_func("a")
    expected_tuples = [('a', 1)]
    expected_split = ['a']
    assert result[0] == expected_tuples
    assert result[1] == expected_split

    # Test case 4: Empty string
    result = task_func("")
    expected_tuples = []
    expected_split = []
    assert result[0] == expected_tuples
    assert result[1] == expected_split

    # Test case 5: Word with no clear split
    result = task_func("abc")
    expected_tuples = [('a', 1), ('b', 2), ('c', 3)]
    expected_split = ['abc']
    assert result[0] == expected_tuples
    assert result[1] == expected_split