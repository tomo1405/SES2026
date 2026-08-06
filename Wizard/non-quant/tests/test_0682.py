python
import json
import pandas as pd
import pytest

from src_0682 import task_func

def test_task_func():
    # Test case 1: Valid input
    input_file = 'data.json'
    input_key = 'key1'
    expected_output = pd.DataFrame({'key2': [1, 2, 3], 'key3': [4, 5, 6]})

    with open(input_file, 'w') as file:
        json.dump({'key1': [1, 2, 3], 'key2': [4, 5, 6]}, file)

    task_func(input_file, input_key)

    with open(input_file, 'r') as file:
        output = pd.read_json(file.read(), orient='records')

    assert output.equals(expected_output)

    # Test case 2: Invalid input (file not found)
    input_file = 'invalid_file.json'
    input_key = 'key1'

    with pytest.raises(FileNotFoundError):
        task_func(input_file, input_key)

    # Test case 3: Invalid input (key not found)
    input_file = 'data.json'
    input_key = 'invalid_key'

    with open(input_file, 'w') as file:
        json.dump({'key1': [1, 2, 3], 'key2': [4, 5, 6]}, file)

    with pytest.raises(KeyError):
        task_func(input_file, input_key)