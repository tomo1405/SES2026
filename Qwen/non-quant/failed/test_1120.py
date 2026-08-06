import pytest
from src_1120 import task_func

def test_task_func_default_parameters():
    hashed_password = task_func()
    assert isinstance(hashed_password, str)
    assert len(hashed_password) == 64  # SHA-256 hash length

def test_task_func_custom_length():
    hashed_password = task_func(password_length=15)
    assert isinstance(hashed_password, str)
    assert len(hashed_password) == 64  # SHA-256 hash length

def test_task_func_custom_salt():
    hashed_password = task_func(salt="custom_salt")
    assert isinstance(hashed_password, str)
    assert len(hashed_password) == 64  # SHA-256 hash length

def test_task_func_same_input_same_output():
    hashed_password_1 = task_func(password_length=10, salt="salty")
    hashed_password_2 = task_func(password_length=10, salt="salty")
    assert hashed_password_1 == hashed_password_2

def test_task_func_different_salt_different_output():
    hashed_password_1 = task_func(password_length=10, salt="salty")
    hashed_password_2 = task_func(password_length=10, salt="another_salt")
    assert hashed_password_1 != hashed_password_2

def test_task_func_different_length_different_output():
    hashed_password_1 = task_func(password_length=10, salt="salty")
    hashed_password_2 = task_func(password_length=15, salt="salty")
    assert hashed_password_1 != hashed_password_2