import pytest
from src_0534 import task_func

def test_task_func_base_conversion():
    num = '101'
    from_base = 2
    to_base = 10
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/'
    
    result, _ = task_func(num, from_base, to_base, alphabet)
    assert result is not None, "The result should not be None"

def test_task_func_invalid_to_base():
    num = '101'
    from_base = 2
    to_base = 1
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/'
    
    with pytest.raises(ValueError) as excinfo:
        task_func(num, from_base, to_base, alphabet)
    assert str(excinfo.value) == "to_base must be >= 2."

def test_task_func_non_numeric_input():
    num = 'abc'
    from_base = 10
    to_base = 2
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/'
    
    with pytest.raises(ValueError) as excinfo:
        task_func(num, from_base, to_base, alphabet)
    assert str(excinfo.value).startswith("invalid literal for int() with base 10:")

def test_task_func_salt_length():
    num = '101'
    from_base = 2
    to_base = 10
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/'
    
    _, salt = task_func(num, from_base, to_base, alphabet)
    assert len(salt) == 32, "Salt should be 32 characters long"

def test_task_func_hashing():
    num = '101'
    from_base = 2
    to_base = 10
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/'
    
    result, _ = task_func(num, from_base, to_base, alphabet)
    assert result is not None, "The result should not be None"
    assert isinstance(result, str), "The result should be a string"