from src_0467 import task_func


def test_task_func():
    my_obj = {
        "color": Color.RED,
        "name": "John Doe",
        "age": 30
    }
    expected_result = '{"color": "RED", "name": "John Doe", "age": 30}'
    assert task_func(my_obj) == expected_result

def test_task_func_with_invalid_input():
    my_obj = {
        "color": "RED",
        "name": "John Doe",
        "age": 30
    }
    expected_result = '{"color": "RED", "name": "John Doe", "age": 30}'
    assert task_func(my_obj) == expected_result

def test_task_func_with_invalid_input_type():
    my_obj = {
        "color": 1,
        "name": "John Doe",
        "age": 30
    }
    expected_result = '{"color": 1, "name": "John Doe", "age": 30}'
    assert task_func(my_obj) == expected_result