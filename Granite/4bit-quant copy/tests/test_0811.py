import re
import os
import subprocess
import pytest

def task_func(dir_path, exe_pattern, execute_files=True):
    results = []
    for dirpath, dirnames, filenames in os.walk(os.path.normpath(dir_path)):
        for filename in filenames:
            if re.search(exe_pattern, filename):
                file_path = os.path.join(dirpath, filename)
                if execute_files:
                    result = subprocess.run([file_path], stdout=subprocess.PIPE)
                    results.append(result.stdout.decode('utf-8'))
                else:
                    results.append(file_path)
    return results

def test_task_func():
    dir_path = "/path/to/directory"
    exe_pattern = r".*\.exe$"
    execute_files = True
    expected_results = ["output1", "output2", "output3"]
    
    results = task_func(dir_path, exe_pattern, execute_files)
    
    assert results == expected_results