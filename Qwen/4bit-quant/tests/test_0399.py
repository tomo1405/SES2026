import os

from src_0399 import task_func


def test_task_func_non_existent_file():
    assert task_func('non_existent_file.json') is False

def test_task_func_invalid_json():
    with open('invalid_json.json', 'w') as f:
        f.write('{')
    assert task_func('invalid_json.json') is False
    os.remove('invalid_json.json')

def test_task_func_valid_json_list_of_dicts():
    with open('valid_json.json', 'w') as f:
        f.write('[{"key": "value"}, {"another_key": "another_value"}]')
    assert task_func('valid_json.json') is True
    os.remove('valid_json.json')

def test_task_func_valid_json_not_list_of_dicts():
    with open('not_list_of_dicts.json', 'w') as f:
        f.write('{"key": "value"}')
    assert task_func('not_list_of_dicts.json') is False
    os.remove('not_list_of_dicts.json')

def test_task_func_empty_file():
    with open('empty_file.json', 'w') as f:
        pass
    assert task_func('empty_file.json') is False
    os.remove('empty_file.json')