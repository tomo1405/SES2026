python
import json
import csv
import numpy as np
from collections import defaultdict
from src_0764 import task_func

def test_task_func():
    input_file = 'input.json'
    output_file = 'output.csv'
    data = [
        {'name': 'John', 'age': 25, 'gender': 'male'},
        {'name': 'Jane', 'age': 30, 'gender': 'female'},
        {'name': 'Bob', 'age': 20, 'gender': 'male'},
        {'name': 'Alice', 'age': 35, 'gender': 'female'}
    ]
    with open(input_file, 'w') as f:
        json.dump(data, f)
    
    task_func(input_file, output_file)
    
    with open(output_file, 'r') as f:
        reader = csv.DictReader(f)
        rows = [row for row in reader]
    
    assert rows == [
        {'key': 'name', 'mean': '25.0', 'median': '25.0'},
        {'key': 'age', 'mean': '25.0', 'median': '25.0'},
        {'key': 'gender', 'mean': '25.0', 'median': '25.0'}
    ]