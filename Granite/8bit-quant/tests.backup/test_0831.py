import json
import os
import pytest
from src_0831 import task_func

def test_task_func():
    filename = 'test.json'
    data = {'key': 'value'}
    success, written_data = task_func(filename, data)
    assert success == True
    assert written_data == data
    os.remove(filename)  # clean up the file after testing

def test_task_func_with_exception():
    filename = 'test.json'
    data = 'not a dictionary'
    success, written_data = task_func(filename, data)
    assert success == False
    assert written_data is None
    os.remove(filename)  # clean up the file after testing