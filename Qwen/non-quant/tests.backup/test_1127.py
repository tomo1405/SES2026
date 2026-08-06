import pytest
from src_1127 import task_func

def test_task_func_with_alphanumeric_input():
    assert task_func("abc123") == "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"

def test_task_func_with_special_characters():
    assert task_func("a!b@c#d$e%") == "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"

def test_task_func_with_spaces():
    assert task_func("a b c") == "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"

def test_task_func_with_empty_string():
    assert task_func("") == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"

def test_task_func_with_unicode_characters():
    assert task_func("café") == "f5d3d58503b92e2de1b2a72470935a7b4c9b1e5e8d8e5d1e8e5e8e5e8e5e8e5e"