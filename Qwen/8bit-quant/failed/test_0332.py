import pytest
from src_0332 import task_func

def test_task_func():
    # Test with default parameters
    num = 5
    numbers, sorted_list = task_func(num)
    assert len(numbers) == 5
    assert len(sorted_list) == 6
    assert num in sorted_list
    assert all(min_value <= x <= max_value for x in numbers)

    # Test with custom list length
    num = 10
    list_length = 10
    numbers, sorted_list = task_func(num, list_length=list_length)
    assert len(numbers) == list_length
    assert len(sorted_list) == list_length + 1
    assert num in sorted_list
    assert all(min_value <= x <= max_value for x in numbers)

    # Test with custom min and max values
    num = 15
    min_value = 5
    max_value = 20
    numbers, sorted_list = task_func(num, min_value=min_value, max_value=max_value)
    assert len(numbers) == 5
    assert len(sorted_list) == 6
    assert num in sorted_list
    assert all(min_value <= x <= max_value for x in numbers)

    # Test with num outside the range of generated numbers
    num = 100
    numbers, sorted_list = task_func(num)
    assert len(numbers) == 5
    assert len(sorted_list) == 6
    assert num in sorted_list
    assert all(min_value <= x <= max_value for x in numbers)

    # Test with num equal to one of the generated numbers
    num = random.randint(0, 0)
    numbers, sorted_list = task_func(num)
    assert len(numbers) == 5
    assert len(sorted_list) == 6
    assert num in sorted_list
    assert all(min_value <= x <= max_value for x in numbers)