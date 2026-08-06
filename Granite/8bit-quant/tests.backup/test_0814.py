import pytest
from src_0814 import task_func

def test_task_func():
    number_list = [1, 2, 3, 4, 5]
    element = 6
    expected_output = pd.DataFrame({'Combinations': [(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5)]})
    actual_output = task_func(number_list, element)
    assert actual_output.equals(expected_output)