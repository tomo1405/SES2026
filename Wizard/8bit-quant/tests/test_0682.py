python
import pandas as pd
import json
import pytest

def task_func(file_path, key):
    with open(file_path, 'r') as file:
        data = json.load(file)

    df = pd.DataFrame(data)
    df.drop(key, axis=1, inplace=True)

    with open(file_path, 'w') as file:
        file.write(df.to_json(orient='records'))

    return df

def test_task_func():
    # Test case 1: Valid input
    input_file_path = 'data.json'
    input_key = 'id'
    expected_output = pd.DataFrame({'name': ['John', 'Jane'], 'age': [30, 25]})
    task_func(input_file_path, input_key)
    actual_output = pd.read_json(input_file_path)
    assert actual_output.equals(expected_output)

    # Test case 2: Invalid input
    input_file_path = 'data.json'
    input_key = 'id'
    expected_output = pd.DataFrame({'name': ['John', 'Jane'], 'age': [30, 25]})
    task_func(input_file_path, input_key)
    actual_output = pd.read_json(input_file_path)
    assert actual_output.equals(expected_output)