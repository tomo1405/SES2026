import pandas as pd
from src_0902 import task_func


def test_task_func_empty_input():
    # Test the function with an empty input list
    input_list = []
    expected_output = pd.DataFrame(columns=['x', 'y', 'z'])
    assert task_func(input_list).equals(expected_output)

def test_task_func_non_empty_input():
    # Test the function with a non-empty input list
    input_list = [{'x': 1, 'y': 2, 'z': 3}, {'x': 4, 'y': 5, 'z': 6}]
    expected_output = pd.DataFrame(data=[(1, 2, 3), (4, 5, 6)], columns=['x', 'y', 'z'])
    assert task_func(input_list).equals(expected_output)