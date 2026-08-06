import pytest
from src_0811 import task_func

def test_task_func():
    # Test case 1: execute_files=True
    dir_path = 'path/to/directory'
    exe_pattern = '.*\.exe$'
    execute_files = True
    results = task_func(dir_path, exe_pattern, execute_files)
    assert len(results) == 2
    assert results[0] == 'output1'
    assert results[1] == 'output2'

    # Test case 2: execute_files=False
    dir_path = 'path/to/directory'
    exe_pattern = '.*\.exe$'
    execute_files = False
    results = task_func(dir_path, exe_pattern, execute_files)
    assert len(results) == 2
    assert results[0] == 'path/to/directory/file1.exe'
    assert results[1] == 'path/to/directory/file2.exe'