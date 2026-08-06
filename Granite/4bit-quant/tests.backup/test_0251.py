import numpy as np
import itertools
import json
from src_0251 import task_func

def test_task_func():
    data_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_results = {'Position 1': 5.0, 'Position 2': 7.0, 'Position 3': 9.0}
    actual_results = task_func(data_list)
    assert actual_results == expected_results

def test_task_func_with_json_file():
    data_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_results = {'Position 1': 5.0, 'Position 2': 7.0, 'Position 3': 9.0}
    with open('mean_values.json', 'w') as f:
        json.dump(expected_results, f)
    actual_results = task_func(data_list)
    assert actual_results == expected_results
    with open('mean_values.json', 'r') as f:
        actual_json_results = json.load(f)
    assert actual_json_results == expected_results