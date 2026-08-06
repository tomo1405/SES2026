import json

from src_0399 import task_func


def test_task_func_valid_json():
    file_path = 'test_data.json'
    with open(file_path, 'w') as file:
        json.dump([{'key': 'value'}], file)

    assert task_func(file_path) == True

def test_task_func_invalid_json():
    file_path = 'test_data.json'
    with open(file_path, 'w') as file:
        json.dump({'key': 'value'}, file)

    assert task_func(file_path) == False

def test_task_func_non_existent_file():
    file_path = 'non_existent_file.json'
    assert task_func(file_path) == False