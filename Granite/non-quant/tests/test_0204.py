import pytest
from src_0204 import task_func

def test_task_func():
    input_data = '{"recipient": "recipient@example.com", "names": ["Alice", "Bob", "Charlie"]}'
    expected_output = ['Alice', 'Bob', 'Charlie']
    
    output = task_func(input_data)
    
    assert output == expected_output, "Output does not match expected output"

def test_task_func_with_invalid_input():
    input_data = "invalid input"
    expected_output = []
    
    output = task_func(input_data)
    
    assert output == expected_output, "Output does not match expected output"

def test_task_func_with_missing_recipient_email():
    input_data = '{"names": ["Alice", "Bob", "Charlie"]}'
    expected_output = []
    
    output = task_func(input_data)
    
    assert output == expected_output, "Output does not match expected output"

def test_task_func_with_missing_names():
    input_data = '{"recipient": "recipient@example.com"}'
    expected_output = []
    
    output = task_func(input_data)
    
    assert output == expected_output, "Output does not match expected output"