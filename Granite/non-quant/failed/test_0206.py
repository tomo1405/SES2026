import subprocess
from multiprocessing import Pool
from pytest import mark

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

@mark.parametrize("commands, expected_outputs", [
    ([], []),
    (["ls", "echo hello"], ["output of ls", "output of echo hello"]),
    (["ls", "echo hello", "echo world"], ["output of ls", "output of echo hello", "output of echo world"]),
])
def test_task_func(commands, expected_outputs):
    assert task_func(commands) == expected_outputs