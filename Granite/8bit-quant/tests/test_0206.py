import pytest
from src_0206 import task_func

def test_task_func():
    commands = ["ls", "echo 'Hello, World!'"]
    expected_outputs = ["list of files in the current directory", "Hello, World!"]

    outputs = task_func(commands)

    assert outputs == expected_outputs

def test_task_func_with_empty_commands():
    commands = []
    expected_outputs = []

    outputs = task_func(commands)

    assert outputs == expected_outputs