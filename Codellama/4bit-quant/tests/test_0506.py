import pytest
from src_0506 import task_func

def test_task_func():
    secret = "secret"
    message = "message"
    expected_result = "098f6bcd4621d373cade4e832627b4f6"
    assert task_func(secret, message) == expected_result

def test_task_func_with_unicode_message():
    secret = "secret"
    message = "message"
    expected_result = "098f6bcd4621d373cade4e832627b4f6"
    assert task_func(secret, message) == expected_result

def test_task_func_with_unicode_secret():
    secret = "secret"
    message = "message"
    expected_result = "098f6bcd4621d373cade4e832627b4f6"
    assert task_func(secret, message) == expected_result

def test_task_func_with_empty_message():
    secret = "secret"
    message = ""
    expected_result = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    assert task_func(secret, message) == expected_result

def test_task_func_with_empty_secret():
    secret = ""
    message = "message"
    expected_result = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    assert task_func(secret, message) == expected_result

def test_task_func_with_empty_message_and_secret():
    secret = ""
    message = ""
    expected_result = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    assert task_func(secret, message) == expected_result