import subprocess
import os
import glob
import time
import pytest

def task_func(test_dir):
    execution_times = {}
    py_scripts = glob.glob(os.path.join(test_dir, '*.py'))

    for py_script in py_scripts:
        start_time = time.time()
        subprocess.call(['python', py_script])
        end_time = time.time()
        execution_times[os.path.basename(py_script)] = end_time - start_time

    return execution_times

def test_task_func():
    test_dir = 'path/to/test/directory'
    execution_times = task_func(test_dir)
    assert isinstance(execution_times, dict)
    for script_name, execution_time in execution_times.items():
        assert isinstance(script_name, str)
        assert isinstance(execution_time, float)
        assert execution_time >= 0