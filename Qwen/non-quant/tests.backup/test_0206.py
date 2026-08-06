import pytest
from src_0206 import execute_command, task_func

def test_execute_command():
    # Test a simple command that should succeed
    result = execute_command("echo Hello, World!")
    assert result.decode('utf-8').strip() == "Hello, World!"

    # Test a command that should fail
    result = execute_command("invalid_command")
    assert result.decode('utf-8').strip() != ""

def test_task_func():
    # Test with a list of commands
    commands = ["echo Hello, World!", "echo Goodbye, World!"]
    results = task_func(commands)
    assert len(results) == len(commands)
    assert results[0].decode('utf-8').strip() == "Hello, World!"
    assert results[1].decode('utf-8').strip() == "Goodbye, World!"

    # Test with an empty list of commands
    results = task_func([])
    assert results == []

    # Test with a single command
    commands = ["echo Single Command"]
    results = task_func(commands)
    assert len(results) == 1
    assert results[0].decode('utf-8').strip() == "Single Command"

    # Test with a command that should fail
    commands = ["invalid_command"]
    results = task_func(commands)
    assert len(results) == 1
    assert results[0].decode('utf-8').strip() != ""