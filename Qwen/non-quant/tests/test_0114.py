import pytest
from src_0114 import task_func
import os
import json
from collections import Counter

def test_task_func_keys_length():
    with pytest.raises(ValueError):
        task_func({}, [1, 2, 3, 4, 5, 6, 7, 8, 9])

def test_task_func_keys_unique():
    with pytest.raises(ValueError):
        task_func({}, [1, 1, 2, 3, 4, 5, 6, 7, 8, 9])

def test_task_func_files_creation():
    my_dict = {}
    keys = list(range(1, 11))
    result_dict, json_filename, txt_filename = task_func(my_dict, keys)

    assert os.path.exists(json_filename)
    assert os.path.exists(txt_filename)

    os.remove(json_filename)
    os.remove(txt_filename)

def test_task_func_json_content():
    my_dict = {'a': 1, 'b': 2}
    keys = list(range(1, 11))
    result_dict, json_filename, txt_filename = task_func(my_dict, keys)

    with open(json_filename, 'r') as json_file:
        loaded_dict = json.load(json_file)

    assert set(result_dict.keys()) == set(my_dict.keys()).union(set(keys))
    assert all(isinstance(value, int) and 1 <= value <= 100 for value in result_dict.values())

    os.remove(json_filename)
    os.remove(txt_filename)

def test_task_func_txt_content():
    my_dict = {'a': 1, 'b': 2}
    keys = list(range(1, 11))
    result_dict, json_filename, txt_filename = task_func(my_dict, keys)

    with open(txt_filename, 'r') as txt_file:
        lines = txt_file.readlines()

    key_counts = Counter(result_dict.keys())
    expected_lines = [f"{key}: {count}\n" for key, count in key_counts.items()]

    assert lines == expected_lines

    os.remove(json_filename)
    os.remove(txt_filename)