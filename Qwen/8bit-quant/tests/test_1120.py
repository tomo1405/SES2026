import pytest
from src_1120 import task_func

def test_task_func_default_parameters():
    result = task_func()
    assert len(result) == 64  # SHA-256 hash length

def test_task_func_custom_length():
    result = task_func(password_length=15)
    assert len(result) == 64  # SHA-256 hash length

def test_task_func_custom_salt():
    result = task_func(salt="pepper")
    assert len(result) == 64  # SHA-256 hash length

def test_task_func_empty_salt():
    result = task_func(salt="")
    assert len(result) == 64  # SHA-256 hash length

def test_task_func_no_punctuation():
    result = task_func(password_length=10, salt="salty")
    assert all(c.isalnum() or c.isspace() for c in result)

def test_task_func_consistency():
    result1 = task_func(password_length=10, salt="salty")
    result2 = task_func(password_length=10, salt="salty")
    assert result1 != result2  # Passwords are random, hashes should differ

def test_task_func_hash_consistency():
    result1 = task_func(password_length=10, salt="salty")
    result2 = task_func(password_length=10, salt="salty")
    assert result1 == result2  # Hashes should be consistent for the same input