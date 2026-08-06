import pytest
from src_0206 import task_func

def test_task_func_with_empty_commands():
    assert task_func([]) == []

def test_task_func_with_single_command():
    expected_output = b'Hello, World!\n'
    assert task_func(['echo "Hello, World!"']) == [expected_output]

def test_task_func_with_multiple_commands():
    expected_outputs = [
        b'Hello, World!\n',
        b'Goodbye, World!\n'
    ]
    assert task_func(['echo "Hello, World!"', 'echo "Goodbye, World!"']) == expected_outputs

def test_task_func_with_invalid_command():
    expected_output = b''
    assert task_func(['invalid_command']) == [expected_output]

def test_task_func_with_mixed_valid_and_invalid_commands():
    expected_outputs = [
        b'Hello, World!\n',
        b''
    ]
    assert task_func(['echo "Hello, World!"', 'invalid_command']) == expected_outputs