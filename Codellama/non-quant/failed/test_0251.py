import pytest
from src_0251 import task_func
import numpy as np
import itertools
import json

def test_task_func():
    data_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    json_file_name = "mean_values.json"
    expected_results = {'Position 1': 4.0, 'Position 2': 5.0, 'Position 3': 6.0}

    results = task_func(data_list, json_file_name)

    assert results == expected_results

    with open(json_file_name, 'r') as f:
        actual_results = json.load(f)

    assert actual_results == expected_results