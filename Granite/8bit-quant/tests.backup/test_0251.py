import pytest
from src_0251 import task_func
import numpy as np
import itertools
import json

def test_task_func():
    data_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_results = {'Position 1': 5.0, 'Position 2': 7.0, 'Position 3': 9.0}

    with open('mean_values.json', 'w') as f:
        json.dump(expected_results, f)

    results = task_func(data_list)

    assert results == expected_results

def test_task_func_with_nan():
    data_list = [[1, 2, np.nan], [4, 5, 6], [7, 8, 9]]
    expected_results = {'Position 1': 4.5, 'Position 2': 6.0, 'Position 3': 9.0}

    with open('mean_values.json', 'w') as f:
        json.dump(expected_results, f)

    results = task_func(data_list)

    assert results == expected_results