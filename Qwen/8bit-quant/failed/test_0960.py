import pytest
from src_0960 import task_func

def test_task_func_no_seed():
    result = task_func("Hello World!")
    assert len(result) == len("Hello World!")
    assert all(c.isalpha() or c.isspace() for c in result)

def test_task_func_with_seed():
    seed_value = 42
    result1 = task_func("Hello World!", seed=seed_value)
    result2 = task_func("Hello World!", seed=seed_value)
    assert result1 == result2

def test_task_func_empty_string():
    result = task_func("")
    assert result == ""

def test_task_func_non_alpha_characters():
    result = task_func("1234!@#$")
    assert result == "1234!@#$"

def test_task_func_mixed_case():
    result = task_func("aBcDeF")
    assert result.lower() == "abcdef"
    assert result.upper() == "ABCDEF"

def test_task_func_whitespace_handling():
    result = task_func("   ")
    assert result == "   "