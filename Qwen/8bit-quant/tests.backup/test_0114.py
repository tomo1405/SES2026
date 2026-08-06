import pytest
from src_0114 import task_func
from collections import Counter
import os

def test_task_func():
    # Prepare test data
    my_dict = {'a': 1, 'b': 2}
    keys = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10']

    # Call the function
    result_dict, json_filename, txt_filename = task_func(my_dict, keys)

    # Check if the dictionary has been updated with 10 new keys
    assert len(result_dict) == 12  # original 2 keys + 10 new keys
    assert all(key in result_dict for key in keys)
    assert all(isinstance(value, int) and 1 <= value <= 100 for value in result_dict.values())

    # Check if the JSON file has been created and contains the correct data
    assert os.path.exists(json_filename)
    with open(json_filename, 'r') as json_file:
        loaded_dict = json.load(json_file)
    assert loaded_dict == result_dict

    # Check if the TXT file has been created and contains the correct key frequencies
    assert os.path.exists(txt_filename)
    with open(txt_filename, 'r') as txt_file:
        lines = txt_file.readlines()
    key_counts = Counter(result_dict.keys())
    for line in lines:
        key, count = line.strip().split(': ')
        assert key_counts[key] == int(count)

    # Clean up files after test
    os.remove(json_filename)
    os.remove(txt_filename)

def test_task_func_invalid_keys_length():
    my_dict = {}
    keys = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9']  # Only 9 keys

    with pytest.raises(ValueError, match="keys parameter must contain exactly 10 unique elements"):
        task_func(my_dict, keys)

def test_task_func_duplicate_keys():
    my_dict = {}
    keys = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x9']  # Duplicate 'x9'

    with pytest.raises(ValueError, match="keys parameter must contain exactly 10 unique elements"):
        task_func(my_dict, keys)