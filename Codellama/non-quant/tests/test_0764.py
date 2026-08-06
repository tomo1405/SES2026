import pytest
from src_0764 import task_func
import numpy as np
from collections import defaultdict
import json
import csv

def test_task_func():
    input_file = 'input.json'
    output_file = 'output.csv'
    data = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}, {'a': 5, 'b': 6}]
    with open(input_file, 'w') as f:
        json.dump(data, f)

    result = task_func(input_file, output_file)

    assert result == {'a': {'mean': 3, 'median': 3}, 'b': {'mean': 3.5, 'median': 3.5}}

    with open(output_file, 'r') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    assert rows == [{'key': 'a', 'mean': 3, 'median': 3}, {'key': 'b', 'mean': 3.5, 'median': 3.5}]