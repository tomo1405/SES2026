import pytest
from src_0274 import task_func

def test_task_func():
    request_handler = task_func()
    assert request_handler.do_POST() == 200

def test_task_func_invalid_content_type():
    request_handler = task_func()
    assert request_handler.do_POST() == 400

def test_task_func_invalid_json():
    request_handler = task_func()
    assert request_handler.do_POST() == 400

def test_task_func_no_data_key():
    request_handler = task_func()
    assert request_handler.do_POST() == 400