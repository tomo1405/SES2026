import pytest
from src_0114 import task_func
import os
import json
from collections import Counter

def test_task_func():
    # Prepare test data
    my_dict = {'a': 1, 'b': 2}
    keys = ['k1', 'k2', 'k3', 'k4', 'k5', 'k6', 'k7', 'k8', 'k9', 'k10']

    # Call the function
    result_dict, json_filename, txt_filename = task_func(my_dict, keys)

    # Check if the dictionary has been updated with 10 new keys
    assert len(result_dict) == 12  # original 2 keys + 10 new keys

    # Check if the JSON file is created and contains the correct data
    assert os.path.exists(json_filename)
    with open(json_filename, 'r') as json_file:
        loaded_dict = json.load(json_file)
    assert loaded_dict == result_dict

    # Check if the text file is created and contains the correct key frequencies
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
    # Prepare test data with invalid number of keys
    my_dict = {'a': 1, 'b': 2}
    keys = ['k1', 'k2', 'k3', 'k4', 'k5', 'k6', 'k7', 'k8', 'k9']

    # Expect a ValueError to be raised
    with pytest.raises(ValueError, match="keys parameter must contain exactly 10 unique elements"):
        task_func(my_dict, keys)

def test_task_func_duplicate_keys():
    # Prepare test data with duplicate keys
    my_dict = {'a': 1, 'b': 2}
    keys = ['k1', 'k2', 'k3', 'k4', 'k5', 'k6', 'k7', 'k8', 'k9', 'k9']

    # Expect a ValueError to be raised due to non-unique keys
    with pytest.raises(ValueError, match="keys parameter must contain exactly 10 unique elements"):
        task_func(my_dict, keys)