import pytest
from src_0730 import task_func

def test_task_func():
    # Test with a list of strings
    strings = ["hello", "world", "test"]
    loaded_strings = task_func(strings)
    assert loaded_strings == strings

    # Test with a single string
    string = "hello"
    loaded_strings = task_func(string)
    assert loaded_strings == [string]

    # Test with a list of integers
    integers = [1, 2, 3]
    loaded_integers = task_func(integers)
    assert loaded_integers == integers

    # Test with a single integer
    integer = 1
    loaded_integers = task_func(integer)
    assert loaded_integers == [integer]

    # Test with a list of floats
    floats = [1.1, 2.2, 3.3]
    loaded_floats = task_func(floats)
    assert loaded_floats == floats

    # Test with a single float
    float = 1.1
    loaded_floats = task_func(float)
    assert loaded_floats == [float]

    # Test with a list of booleans
    booleans = [True, False, True]
    loaded_booleans = task_func(booleans)
    assert loaded_booleans == booleans

    # Test with a single boolean
    boolean = True
    loaded_booleans = task_func(boolean)
    assert loaded_booleans == [boolean]

    # Test with a list of None
    none_list = [None, None, None]
    loaded_none_list = task_func(none_list)
    assert loaded_none_list == none_list

    # Test with a single None
    none = None
    loaded_none = task_func(none)
    assert loaded_none == [none]

    # Test with a list of mixed types
    mixed_list = [1, "hello", 2.2, True, None]
    loaded_mixed_list = task_func(mixed_list)
    assert loaded_mixed_list == mixed_list

    # Test with a single mixed type
    mixed = 1
    loaded_mixed = task_func(mixed)
    assert loaded_mixed == [mixed]