import pytest
from src_1022 import task_func

def test_task_func_input_string():
    input_string = "hello world"
    verify_hash = None
    expected_output = "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9"
    assert task_func(input_string, verify_hash) == expected_output

def test_task_func_input_string_verify_hash():
    input_string = "hello world"
    verify_hash = "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9"
    assert task_func(input_string, verify_hash) == True

def test_task_func_input_string_verify_hash_mismatch():
    input_string = "hello world"
    verify_hash = "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde8"
    assert task_func(input_string, verify_hash) == False

def test_task_func_input_string_verify_hash_none():
    input_string = "hello world"
    verify_hash = None
    expected_output = "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9"
    assert task_func(input_string, verify_hash) == expected_output

def test_task_func_input_string_verify_hash_invalid():
    input_string = "hello world"
    verify_hash = "invalid"
    with pytest.raises(TypeError):
        task_func(input_string, verify_hash)