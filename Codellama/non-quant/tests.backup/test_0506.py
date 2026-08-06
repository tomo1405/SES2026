import pytest
from src_0506 import task_func

def test_task_func():
    secret = "secret"
    message = "message"
    expected_result = "098f6bcd4621d373cade4e832627b4f6"
    assert task_func(secret, message) == expected_result

def test_task_func_with_different_message():
    secret = "secret"
    message = "different message"
    expected_result = "9ae16a3b2fed1c3a053041042ed93196"
    assert task_func(secret, message) == expected_result

def test_task_func_with_different_secret():
    secret = "different secret"
    message = "message"
    expected_result = "5d41402abc4b2a76b9719d911017c592"
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