import pytest
from src_0764 import task_func
import numpy as np
import json
import csv
from io import StringIO

def test_task_func_with_valid_json():
    input_data = '[{"a": 1, "b": 2}, {"a": 3, "b": 4}]'
    input_file = StringIO(input_data)
    output_file = StringIO()

    expected_result = {
        'a': {'mean': 2.0, 'median': 2.0},
        'b': {'mean': 3.0, 'median': 3.0}
    }

    result = task_func(input_file, output_file)

    assert result == expected_result

    output_file.seek(0)
    reader = csv.DictReader(output_file)
    rows = list(reader)

    assert rows == [
        {'key': 'a', 'mean': '2.0', 'median': '2.0'},
        {'key': 'b', 'mean': '3.0', 'median': '3.0'}
    ]

def test_task_func_with_empty_json():
    input_data = '[]'
    input_file = StringIO(input_data)
    output_file = StringIO()

    expected_result = {}

    result = task_func(input_file, output_file)

    assert result == expected_result

    output_file.seek(0)
    reader = csv.DictReader(output_file)
    rows = list(reader)

    assert rows == []

def test_task_func_with_single_element_json():
    input_data = '[{"a": 5}]'
    input_file = StringIO(input_data)
    output_file = StringIO()

    expected_result = {
        'a': {'mean': 5.0, 'median': 5.0}
    }

    result = task_func(input_file, output_file)

    assert result == expected_result

    output_file.seek(0)
    reader = csv.DictReader(output_file)
    rows = list(reader)

    assert rows == [
        {'key': 'a', 'mean': '5.0', 'median': '5.0'}
    ]

def test_task_func_with_non_numeric_values():
    input_data = '[{"a": "one", "b": 2}, {"a": "two", "b": 4}]'
    input_file = StringIO(input_data)
    output_file = StringIO()

    with pytest.raises(ValueError):
        task_func(input_file, output_file)