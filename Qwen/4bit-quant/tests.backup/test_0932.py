import pytest
from src_0932 import task_func

def test_task_func_empty_string():
    assert task_func("") == {}

def test_task_func_single_character():
    assert task_func("a") == {}

def test_task_func_no_pairs():
    assert task_func("abc") == {'ab': 1, 'bc': 1}

def test_task_func_with_duplicates():
    assert task_func("aabbcc") == {'aa': 1, 'ab': 1, 'bb': 1, 'bc': 1, 'cc': 1}

def test_task_func_with_special_characters():
    assert task_func("a!b@c#") == {'ab': 1}

def test_task_func_mixed_case():
    assert task_func("AbcABC") == {'Ab': 1, 'bC': 1, 'cA': 1, 'Ca': 1, 'aB': 1, 'BC': 1}

def test_task_func_large_input():
    large_input = "a" * 1000
    expected_output = {f"{large_input[i]}{large_input[i+1]}": 1 for i in range(len(large_input) - 1)}
    assert task_func(large_input) == expected_output