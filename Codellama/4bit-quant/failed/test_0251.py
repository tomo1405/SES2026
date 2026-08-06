import pytest
from src_0251 import task_func
import numpy as np
import itertools
import json

def test_task_func():
    data_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    json_file_name = "mean_values.json"
    results = task_func(data_list, json_file_name)
    assert results == {'Position 1': 4.0, 'Position 2': 5.0, 'Position 3': 6.0}

    with open(json_file_name, 'r') as f:
        json_data = json.load(f)
    assert json_data == results