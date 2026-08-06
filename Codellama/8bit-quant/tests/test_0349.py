import subprocess

from src_0349 import task_func


def test_task_func_with_no_processes():
    assert task_func('non_existent_process') == 0

def test_task_func_with_one_process():
    # Create a process with the given name
    process = subprocess.Popen(['sleep', '10'])
    try:
        # Call the function with the process name
        assert task_func('sleep') == 1
    finally:
        # Clean up the process
        process.terminate()
        process.wait()

def test_task_func_with_multiple_processes():
    # Create multiple processes with the given name
    processes = [subprocess.Popen(['sleep', '10']) for _ in range(3)]
    try:
        # Call the function with the process name
        assert task_func('sleep') == 3
    finally:
        # Clean up the processes
        for process in processes:
            process.terminate()
            process.wait()