import pytest
from src_0960 import task_func

def test_task_func_with_no_seed():
    result = task_func("Hello World!")
    assert all(c.isalpha() == c.isalpha() for c in result)

def test_task_func_with_seed():
    seed_value = 42
    result1 = task_func("Hello World!", seed=seed_value)
    result2 = task_func("Hello World!", seed=seed_value)
    assert result1 == result2

def test_task_func_empty_string():
    result = task_func("")
    assert result == ""

def test_task_func_all_lowercase():
    seed_value = 42
    result = task_func("abcdef", seed=seed_value)
    assert result == "zjklpq"

def test_task_func_all_uppercase():
    seed_value = 42
    result = task_func("ABCDEF", seed=seed_value)
    assert result == "ZJKLPQ"

def test_task_func_mixed_case():
    seed_value = 42
    result = task_func("aBcDeF", seed=seed_value)
    assert result == "zJkLpQ"

def test_task_func_with_non_alphabetic_characters():
    seed_value = 42
    result = task_func("Hello, World! 123", seed=seed_value)
    assert result == "zJkLpQ, zJkLpQ! 123"