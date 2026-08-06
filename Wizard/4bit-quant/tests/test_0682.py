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
    # Test case 1: Valid input file and key
    file_path = 'data.json'
    key = 'id'
    expected_df = pd.DataFrame({'name': ['John', 'Jane'], 'age': [25, 30]})
    task_func(file_path, key)
    actual_df = pd.read_json(file_path)
    assert actual_df.equals(expected_df)

    # Test case 2: Invalid input file
    file_path = 'invalid_file.json'
    key = 'id'
    with pytest.raises(FileNotFoundError):
        task_func(file_path, key)

    # Test case 3: Invalid key
    file_path = 'data.json'
    key = 'invalid_key'
    expected_df = pd.DataFrame({'name': ['John', 'Jane'], 'age': [25, 30]})
    task_func(file_path, key)
    actual_df = pd.read_json(file_path)
    assert actual_df.equals(expected_df)