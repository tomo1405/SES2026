import pytest
from src_1119 import task_func

def test_task_func():
    json_file_path = task_func()
    assert json_file_path == 'data.json'

def test_task_func_with_custom_csv_url():
    json_file_path = task_func(csv_url='https://example.com/custom-data.csv')
    assert json_file_path == 'data.json'

def test_task_func_with_custom_json_file_path():
    json_file_path = task_func(json_file_path='custom-data.json')
    assert json_file_path == 'custom-data.json'

def test_task_func_with_custom_csv_url_and_json_file_path():
    json_file_path = task_func(csv_url='https://example.com/custom-data.csv', json_file_path='custom-data.json')
    assert json_file_path == 'custom-data.json'