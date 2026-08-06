import pytest
from src_0206 import execute_command, task_func

def test_execute_command():
    command = "echo 'Hello World'"
    output = execute_command(command)
    assert output == b'Hello World\n'

def test_task_func():
    commands = ["echo 'Hello World'", "echo 'Hello Python'"]
    outputs = task_func(commands)
    assert outputs == [b'Hello World\n', b'Hello Python\n']