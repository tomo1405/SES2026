import pytest
from src_0114 import task_func

def test_task_func_keys_length():
    my_dict = {}
    keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    task_func(my_dict, keys)
    assert len(my_dict) == 10

def test_task_func_keys_unique():
    my_dict = {}
    keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    task_func(my_dict, keys)
    assert len(set(my_dict.keys())) == 10

def test_task_func_json_file_created():
    my_dict = {}
    keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    task_func(my_dict, keys)
    assert "updated_dictionary.json" in my_dict

def test_task_func_txt_file_created():
    my_dict = {}
    keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    task_func(my_dict, keys)
    assert "key_frequencies.txt" in my_dict

def test_task_func_json_file_content():
    my_dict = {}
    keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    task_func(my_dict, keys)
    with open("updated_dictionary.json", "r") as json_file:
        json_data = json.load(json_file)
        assert json_data == my_dict

def test_task_func_txt_file_content():
    my_dict = {}
    keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    task_func(my_dict, keys)
    with open("key_frequencies.txt", "r") as txt_file:
        txt_data = txt_file.read()
        assert txt_data == "1: 1\n2: 1\n3: 1\n4: 1\n5: 1\n6: 1\n7: 1\n8: 1\n9: 1\n10: 1\n"