import pytest
from src_0764 import task_func
import numpy as np
from collections import defaultdict
import json
import csv

def test_task_func():
    input_file = 'input.json'
    output_file = 'output.csv'
    data = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]
    with open(input_file, 'w') as f:
        json.dump(data, f)

    result = task_func(input_file, output_file)

    assert result == {'a': {'mean': 2, 'median': 2}, 'b': {'mean': 3, 'median': 3}}

    with open(output_file, 'r') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        assert rows == [{'key': 'a', 'mean': 2, 'median': 2}, {'key': 'b', 'mean': 3, 'median': 3}]