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
    assert result[2] == "key_frequencies.json"
    assert isinstance(my_dict, dict)
    assert len(my_dict) == 10
    for key in keys:
        assert key in my_dict
        assert isinstance(my_dict[key], int)
        assert 1 <= my_dict[key] <= 100
    with open("updated_dictionary.json", "r") as json_file:
        data = json.load(json_file)
        assert data == my_dict
    with open("key_frequencies.txt", "r") as txt_file:
        lines = txt_file.readlines()
        assert len(lines) == 10
        for line in lines:
            key, count = line.strip().split(":")
            assert key in my_dict
            assert int(count) == my_dict[key]

def test_task_func_invalid_keys():
    my_dict = {}
    keys = list(range(11))
    with pytest.raises(ValueError) as exc_info:
        task_func(my_dict, keys)
    assert "keys parameter must contain exactly 10 unique elements" in str(exc_info.value)