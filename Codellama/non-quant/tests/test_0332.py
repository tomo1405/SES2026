import pytest
from src_0332 import task_func

def test_task_func():
    # Test case 1: num is in the middle of the list
    num = 5
    list_length = 5
    min_value = 0
    max_value = 10
    numbers, sorted_list = task_func(num, list_length, min_value, max_value)
    assert numbers == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert sorted_list == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Test case 2: num is at the beginning of the list
    num = 0
    list_length = 5
    min_value = 0
    max_value = 10
    numbers, sorted_list = task_func(num, list_length, min_value, max_value)
    assert numbers == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert sorted_list == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Test case 3: num is at the end of the list
    num = 10
    list_length = 5
    min_value = 0
    max_value = 10
    numbers, sorted_list = task_func(num, list_length, min_value, max_value)
    assert numbers == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert sorted_list == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Test case 4: num is not in the list
    num = 11
    list_length = 5
    min_value = 0
    max_value = 10
    numbers, sorted_list = task_func(num, list_length, min_value, max_value)
    assert numbers == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert sorted_list == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Test case 5: list_length is 0
    num = 5
    list_length = 0
    min_value = 0
    max_value = 10
    numbers, sorted_list = task_func(num, list_length, min_value, max_value)
    assert numbers == []
    assert sorted_list == []

    # Test case 6: min_value is greater than max_value
    num = 5
    list_length = 5
    min_value = 10
    max_value = 0
    with pytest.raises(ValueError):
        task_func(num, list_length, min_value, max_value)