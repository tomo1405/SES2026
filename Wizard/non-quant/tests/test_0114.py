python
import json
from collections import Counter
import random
import pytest

def task_func(my_dict, keys):
    if len(set(keys)) != 10:
        raise ValueError("keys parameter must contain exactly 10 unique elements")

    for key in keys:
        my_dict[key] = random.randint(1, 100)

    json_filename = "updated_dictionary.json"
    txt_filename = "key_frequencies.txt"

    with open(json_filename, 'w') as json_file:
        json.dump(my_dict, json_file, indent=4)

    key_counts = Counter(my_dict.keys())
    with open(txt_filename, 'w') as txt_file:
        for key, count in key_counts.items():
            txt_file.write(f"{key}: {count}\n")

    return my_dict, json_filename, txt_filename

def test_task_func():
    my_dict = {}
    keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    with pytest.raises(ValueError):
        task_func(my_dict, keys)

    my_dict = {}
    keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    my_dict, json_filename, txt_filename = task_func(my_dict, keys)
    assert len(my_dict) == 10
    assert len(set(my_dict.keys())) == 10
    assert all(isinstance(value, int) for value in my_dict.values())
    assert json_filename == "updated_dictionary.json"
    assert txt_filename == "key_frequencies.txt"
    with open(json_filename, 'r') as json_file:
        assert json.load(json_file) == my_dict
    with open(txt_filename, 'r') as txt_file:
        assert txt_file.read() == "a: 1\nb: 1\nc: 1\nd: 1\ne: 1\nf: 1\ng: 1\nh: 1\ni: 1\nj: 1\nk: 1\n"