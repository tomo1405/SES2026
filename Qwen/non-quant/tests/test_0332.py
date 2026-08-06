from src_0332 import task_func


def test_task_func_default_parameters():
    num = 10
    numbers, sorted_list = task_func(num)
    assert len(numbers) == 5
    assert all(min_value <= x <= max_value for x in numbers)
    assert num in sorted_list
    assert sorted_list == sorted(numbers + [num])

def test_task_func_custom_parameters():
    num = 25
    list_length = 7
    min_value = 10
    max_value = 30
    numbers, sorted_list = task_func(num, list_length, min_value, max_value)
    assert len(numbers) == 7
    assert all(min_value <= x <= max_value for x in numbers)
    assert num in sorted_list
    assert sorted_list == sorted(numbers + [num])

def test_task_func_min_max_same():
    num = 15
    min_value = 15
    max_value = 15
    numbers, sorted_list = task_func(num, min_value=min_value, max_value=max_value)
    assert all(x == 15 for x in numbers)
    assert sorted_list == [15] * 6 + [num]

def test_task_func_num_out_of_range():
    num = 5
    min_value = 10
    max_value = 20
    numbers, sorted_list = task_func(num, min_value=min_value, max_value=max_value)
    assert num not in numbers
    assert num in sorted_list
    assert sorted_list[0] == num
    assert all(min_value <= x <= max_value for x in numbers)

def test_task_func_num_within_range():
    num = 15
    min_value = 10
    max_value = 20
    numbers, sorted_list = task_func(num, min_value=min_value, max_value=max_value)
    assert num in numbers
    assert num in sorted_list
    assert sorted_list == sorted(numbers + [num])