import json
from collections import Counter
import random
from src_0114 import task_func
import pytest

def test_task_func():
    my_dict = {}
    keys = list(range(10))
    result = task_func(my_dict, keys)
    assert result[0] == my_dict
    assert result[1] == "updated_dictionary.json"
    assert result[2] == "key_frequencies.txt"
    assert isinstance(my_dict, dict)
    assert len(my_dict) == 10
    for key in keys:
        assert key in my_dict
        assert isinstance(my_dict[key], int)
        assert 1 <= my_dict[key] <= 100
    with open("updated_dictionary.json", "r") as json_file:
        assert json.load(json_file) == my_dict
    with open("key_frequencies.txt", "r") as txt_file:
        key_counts = Counter(my_dict.keys())
        for line in txt_file:
            key, count = line.strip().split(": ")
            assert int(count) == key_counts[key]

def test_task_func_invalid_keys():
    my_dict = {}
    keys = list(range(11))
    with pytest.raises(ValueError):
        task_func(my_dict, keys)