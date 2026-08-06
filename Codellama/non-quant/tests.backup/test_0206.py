import pytest
from src_0206 import execute_command, task_func

def test_execute_command():
    command = "echo 'Hello, World!'"
    output = execute_command(command)
    assert output == b"Hello, World!\n"

def test_task_func():
    commands = ["echo 'Hello, World!'", "echo 'Goodbye, World!'"]
    outputs = task_func(commands)
    assert len(outputs) == 2
    assert outputs[0] == b"Hello, World!\n"
    assert outputs[1] == b"Goodbye, World!\n"