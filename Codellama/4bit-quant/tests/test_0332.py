import pytest
from src_0332 import task_func

def test_task_func():
    # Test case 1: num is not in the list
    num = 10
    list_length = 5
    min_value = 0
    max_value = 10
    numbers, sorted_list = task_func(num, list_length, min_value, max_value)
    assert num in sorted_list
    assert sorted_list == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Test case 2: num is in the list
    num = 5
    list_length = 5
    min_value = 0
    max_value = 10
    numbers, sorted_list = task_func(num, list_length, min_value, max_value)
    assert num in sorted_list
    assert sorted_list == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Test case 3: list_length is 0
    num = 10
    list_length = 0
    min_value = 0
    max_value = 10
    numbers, sorted_list = task_func(num, list_length, min_value, max_value)
    assert num in sorted_list
    assert sorted_list == []

    # Test case 4: min_value is greater than max_value
    num = 10
    list_length = 5
    min_value = 10
    max_value = 0
    with pytest.raises(ValueError):
        task_func(num, list_length, min_value, max_value)

    # Test case 5: num is not an integer
    num = 10.5
    list_length = 5
    min_value = 0
    max_value = 10
    with pytest.raises(TypeError):
        task_func(num, list_length, min_value, max_value)

    # Test case 6: list_length is not an integer
    num = 10
    list_length = 5.5
    min_value = 0
    max_value = 10
    with pytest.raises(TypeError):
        task_func(num, list_length, min_value, max_value)

    # Test case 7: min_value is not an integer
    num = 10
    list_length = 5
    min_value = 0.5
    max_value = 10
    with pytest.raises(TypeError):
        task_func(num, list_length, min_value, max_value)

    # Test case 8: max_value is not an integer
    num = 10
    list_length = 5
    min_value = 0
    max_value = 10.5
    with pytest.raises(TypeError):
        task_func(num, list_length, min_value, max_value)