import subprocess
from multiprocessing import Pool
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
import pytest

def test_task_func():
    commands = ["ls", "pwd"]
    expected_outputs = [b'output1', b'output2']
    outputs = task_func(commands)
    assert outputs == expected_outputs

def test_task_func_with_empty_commands():
    commands = []
    expected_outputs = []
    outputs = task_func(commands)
    assert outputs == expected_outputs