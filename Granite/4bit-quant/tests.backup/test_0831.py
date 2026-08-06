import json
import os
import pytest

def task_func(filename, data):
    try:
        with open(filename, 'w') as f:
            json.dump(data, f)
        
        file_exists = os.path.exists(filename)
        if not file_exists:
            return False, None

        with open(filename, 'r') as f:
            written_data = json.load(f)
            if written_data != data:
                return False, None

        return True, written_data
    except Exception as e:
        return False, None

def test_task_func():
    filename = 'test_file.json'
    data = {'key': 'value'}
    expected_result = (True, data)
    actual_result = task_func(filename, data)
    assert actual_result == expected_result, "Task function returned an incorrect result"

def test_task_func_exception():
    filename = 'test_file.json'
    data = 'not a dictionary'
    expected_result = (False, None)
    actual_result = task_func(filename, data)
    assert actual_result == expected_result, "Task function did not handle exceptions correctly"