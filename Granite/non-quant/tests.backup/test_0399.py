import json
import os
import pytest

from src_0399 import task_func

def test_task_func():
    file_path = 'test_file.json'
    with open(file_path, 'w') as file:
        file.write('not a json string')
    assert not task_func(file_path)
    os.remove(file_path)

    file_path = 'test_file.json'
    with open(file_path, 'w') as file:
        file.write('["valid", "json", "list"]')
    assert task_func(file_path)
    os.remove(file_path)

    file_path = 'test_file.json'
    with open(file_path, 'w') as file:
        file.write('["valid", "json", 123]')
    assert not task_func(file_path)
    os.remove(file_path)