import pytest
from src_0399 import task_func
import os
import json

def test_task_func_file_not_exists():
    assert task_func("non_existent_file.json") == False

def test_task_func_invalid_json():
    with open("temp_invalid.json", "w") as file:
        file.write("invalid json")
    assert task_func("temp_invalid.json") == False
    os.remove("temp_invalid.json")

def test_task_func_valid_json():
    with open("temp_valid.json", "w") as file:
        json.dump([{"key": "value"}, {"another_key": "another_value"}], file)
    assert task_func("temp_valid.json") == True
    os.remove("temp_valid.json")

def test_task_func_empty_list():
    with open("temp_empty_list.json", "w") as file:
        json.dump([], file)
    assert task_func("temp_empty_list.json") == True
    os.remove("temp_empty_list.json")

def test_task_func_non_dict_items():
    with open("temp_non_dict_items.json", "w") as file:
        json.dump(["not a dict", {"key": "value"}], file)
    assert task_func("temp_non_dict_items.json") == False
    os.remove("temp_non_dict_items.json")