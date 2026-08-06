import pytest
from src_0764 import task_func
import numpy as np
import json
import csv
from io import StringIO

def test_task_func_with_valid_data(tmp_path):
    # Create a temporary input file with sample JSON data
    input_data = [
        {"a": 1, "b": 2},
        {"a": 3, "b": 4},
        {"a": 5, "b": 6}
    ]
    input_file = tmp_path / "input.json"
    with open(input_file, 'w') as f:
        json.dump(input_data, f)

    # Create a temporary output file path
    output_file = tmp_path / "output.csv"

    # Call the function
    result = task_func(str(input_file), str(output_file))

    # Check the result dictionary
    expected_result = {
        'a': {'mean': 3.0, 'median': 3.0},
        'b': {'mean': 4.0, 'median': 4.0}
    }
    assert result == expected_result

    # Check the output CSV file
    with open(output_file, 'r') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        assert len(rows) == 2
        assert rows[0] == {'key': 'a', 'mean': '3.0', 'median': '3.0'}
        assert rows[1] == {'key': 'b', 'mean': '4.0', 'median': '4.0'}

def test_task_func_with_empty_input(tmp_path):
    # Create a temporary input file with empty JSON data
    input_data = []
    input_file = tmp_path / "input.json"
    with open(input_file, 'w') as f:
        json.dump(input_data, f)

    # Create a temporary output file path
    output_file = tmp_path / "output.csv"

    # Call the function
    result = task_func(str(input_file), str(output_file))

    # Check the result dictionary
    expected_result = {}
    assert result == expected_result

    # Check the output CSV file
    with open(output_file, 'r') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        assert len(rows) == 0

def test_task_func_with_single_entry(tmp_path):
    # Create a temporary input file with a single entry JSON data
    input_data = [{"a": 10}]
    input_file = tmp_path / "input.json"
    with open(input_file, 'w') as f:
        json.dump(input_data, f)

    # Create a temporary output file path
    output_file = tmp_path / "output.csv"

    # Call the function
    result = task_func(str(input_file), str(output_file))

    # Check the result dictionary
    expected_result = {'a': {'mean': 10.0, 'median': 10.0}}
    assert result == expected_result

    # Check the output CSV file
    with open(output_file, 'r') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        assert len(rows) == 1
        assert rows[0] == {'key': 'a', 'mean': '10.0', 'median': '10.0'}