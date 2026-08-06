python
import subprocess
from multiprocessing import Pool
import pytest

def execute_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, _ = process.communicate()
    return output

def task_func(commands):

    if not commands:  # Handle case where commands list is empty
        return []

    with Pool(processes=len(commands)) as pool:
        outputs = pool.map(execute_command, commands)

    return outputs

def test_task_func():
    # Test case 1: commands list is empty
    assert task_func([]) == []

    # Test case 2: commands list has one command
    commands = ['echo "Hello, world!"']
    expected_output = ['Hello, world!\n']
    assert task_func(commands) == expected_output

    # Test case 3: commands list has multiple commands
    commands = ['echo "Hello, world!"', 'echo "Goodbye, world!"']
    expected_output = ['Hello, world!\n', 'Goodbye, world!\n']
    assert task_func(commands) == expected_output