import json
from collections import Counter
import random
from src_0114 import task_func
import pytest

def test_task_func():
    my_dict = {}
    keys = list(range(10))
    my_dict, json_filename, txt_filename = task_func(my_dict, keys)

    assert isinstance(my_dict, dict)
    assert len(my_dict) == 10
    for key, value in my_dict.items():
        assert isinstance(key, int)
        assert isinstance(value, int)
        assert 1 <= value <= 100

    assert isinstance(json_filename, str)
    assert json_filename == "updated_dictionary.json"

    assert isinstance(txt_filename, str)
    assert txt_filename == "key_frequencies.txt"

def test_task_func_invalid_keys():
    my_dict = {}
    keys = list(range(11))
    with pytest.raises(ValueError) as exc_info:
        task_func(my_dict, keys)
    assert "keys parameter must contain exactly 10 unique elements" in str(exc_info.value)