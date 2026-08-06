import pytest
from src_1127 import task_func

def test_task_func_with_alphanumeric_input():
    assert task_func("abc123") == "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1f8a2bdc11697c6734a0c1"

def test_task_func_with_special_characters():
    assert task_func("abc!@#123$%^") == "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1f8a2bdc11697c6734a0c1"

def test_task_func_with_whitespace():
    assert task_func("  abc 123 ") == "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1f8a2bdc11697c6734a0c1"

def test_task_func_with_empty_string():
    assert task_func("") == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"

def test_task_func_with_mixed_case():
    assert task_func("AbC123") == "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1f8a2bdc11697c6734a0c1"