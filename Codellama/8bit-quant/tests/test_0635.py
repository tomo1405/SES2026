from src_0635 import task_func


def test_task_func_with_empty_list():
    input_list = []
    repetitions = 1
    expected_result = None
    actual_result = task_func(input_list, repetitions)
    assert actual_result == expected_result

def test_task_func_with_single_element_list():
    input_list = [1]
    repetitions = 1
    expected_result = 1
    actual_result = task_func(input_list, repetitions)
    assert actual_result == expected_result

def test_task_func_with_multiple_element_list():
    input_list = [1, 2, 3]
    repetitions = 2
    expected_result = 1
    actual_result = task_func(input_list, repetitions)
    assert actual_result == expected_result

def test_task_func_with_different_repetitions():
    input_list = [1, 2, 3]
    repetitions = 3
    expected_result = 1
    actual_result = task_func(input_list, repetitions)
    assert actual_result == expected_result

def test_task_func_with_different_input_list():
    input_list = [1, 2, 3, 4, 5]
    repetitions = 2
    expected_result = 3
    actual_result = task_func(input_list, repetitions)
    assert actual_result == expected_result