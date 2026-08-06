import pytest
from src_0266 import task_func
import json
import os

def test_task_func():
    data = {'a': 1, 'b': 2, 'c': 1}
    json_file_name = 'data.json'
    json_file_path = task_func(data, json_file_name)
    assert os.path.exists(json_file_path)
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)
    assert json_data['data'] == data
    assert json_data['freq'] == {1: 2, 2: 1}
    os.remove(json_file_path)

def test_task_func_with_default_json_file_name():
    data = {'a': 1, 'b': 2, 'c': 1}
    json_file_path = task_func(data)
    assert os.path.exists(json_file_path)
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)
    assert json_data['data'] == data
    assert json_data['freq'] == {1: 2, 2: 1}
    os.remove(json_file_path)

def test_task_func_with_empty_data():
    data = {}
    json_file_name = 'data.json'
    json_file_path = task_func(data, json_file_name)
    assert os.path.exists(json_file_path)
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)
    assert json_data['data'] == data
    assert json_data['freq'] == {}
    os.remove(json_file_path)

def test_task_func_with_None_data():
    data = None
    with pytest.raises(TypeError):
        task_func(data)