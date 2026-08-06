import pytest
from src_0206 import task_func, execute_command

def test_execute_command():
    command = "echo Hello, World!"
    expected_output = b"Hello, World!\n"
    assert execute_command(command) == expected_output

def test_task_func_single_command():
    commands = ["echo Single Command"]
    expected_output = [b"Single Command\n"]
    assert task_func(commands) == expected_output

def test_task_func_multiple_commands():
    commands = ["echo Command 1", "echo Command 2"]
    expected_output = [b"Command 1\n", b"Command 2\n"]
    assert task_func(commands) == expected_output

def test_task_func_empty_commands():
    commands = []
    expected_output = []
    assert task_func(commands) == expected_output

def test_task_func_with_nonexistent_command():
    commands = ["nonexistent_command"]
    expected_output = [b'']
    assert task_func(commands) == expected_output

def test_task_func_with_error_command():
    commands = ["echo This will fail && exit 1"]
    expected_output = [b'This will fail\n']
    assert task_func(commands) == expected_output