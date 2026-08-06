import math

from src_0683 import task_func


def test_task_func():
    nested_dict = {'a': {'a': 1, 'b': 2}, 'b': {'a': 3, 'b': 4}}
    expected_result = {'a': math.sin(3), 'b': math.sin(6)}
    assert task_func(nested_dict) == expected_result

    nested_dict = {'a': {'a': 1, 'b': 2}, 'b': {'a': 3, 'b': 4}, 'c': {'a': 5, 'b': 6}}
    expected_result = {'a': math.sin(9), 'b': math.sin(12)}
    assert task_func(nested_dict) == expected_result

    nested_dict = {'a': {'a': 1, 'b': 2}, 'b': {'a': 3, 'b': 4}, 'c': {'a': 5, 'b': 6}, 'd': {'a': 7, 'b': 8}}
    expected_result = {'a': math.sin(15), 'b': math.sin(18)}
    assert task_func(nested_dict) == expected_result