from src_0332 import task_func


def test_task_func_with_default_values():
    num = 5
    numbers, sorted_list = task_func(num)
    assert len(numbers) == 5
    assert all(min_value <= n <= max_value for n in numbers)
    assert num in sorted_list
    assert sorted_list == sorted(numbers + [num])

def test_task_func_with_custom_values():
    num = 10
    list_length = 7
    min_value = 1
    max_value = 20
    numbers, sorted_list = task_func(num, list_length, min_value, max_value)
    assert len(numbers) == 7
    assert all(min_value <= n <= max_value for n in numbers)
    assert num in sorted_list
    assert sorted_list == sorted(numbers + [num])

def test_task_func_with_min_max_same():
    num = 5
    min_value = 5
    max_value = 5
    numbers, sorted_list = task_func(num, min_value=min_value, max_value=max_value)
    assert len(numbers) == 5
    assert all(n == 5 for n in numbers)
    assert num in sorted_list
    assert sorted_list == [5, 5, 5, 5, 5, 5]

def test_task_func_with_num_out_of_range():
    num = 25
    min_value = 0
    max_value = 20
    numbers, sorted_list = task_func(num, min_value=min_value, max_value=max_value)
    assert len(numbers) == 5
    assert all(min_value <= n <= max_value for n in numbers)
    assert num in sorted_list
    assert sorted_list == sorted(numbers + [num])

def test_task_func_with_zero_length():
    num = 5
    list_length = 0
    numbers, sorted_list = task_func(num, list_length=list_length)
    assert len(numbers) == 0
    assert sorted_list == [5]