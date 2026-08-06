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
    assert task_func(['ls']) == [b'file1\nfile2\nfile3\n']

    # Test case 3: commands list has multiple commands
    assert task_func(['ls', 'pwd', 'echo hello']) == [b'file1\nfile2\nfile3\n', b'/home/user\n', b'hello\n']