import pytest
from src_0347 import task_func
import os
import sys
import tempfile

def test_task_func_script_not_exists():
    with pytest.raises(ValueError) as excinfo:
        task_func("non_existent_script.py")
    assert "Script 'non_existent_script.py' does not exist." in str(excinfo.value)

def test_task_func_script_with_exception():
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp_file:
        temp_file.write("#!/usr/bin/env python\nraise Exception('Test exception')")
        temp_file.close()
        os.chmod(temp_file.name, 0o755)
    
    try:
        with pytest.raises(subprocess.CalledProcessError):
            task_func(temp_file.name)
    finally:
        os.remove(temp_file.name)

def test_task_func_script_success():
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp_file:
        temp_file.write("#!/usr/bin/env python\nprint('Success')")
        temp_file.close()
        os.chmod(temp_file.name, 0o755)
    
    try:
        return_code = task_func(temp_file.name)
        assert return_code == 0
    finally:
        os.remove(temp_file.name)

def test_task_func_script_no_wait():
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp_file:
        temp_file.write("#!/usr/bin/env python\ntime.sleep(2)")
        temp_file.close()
        os.chmod(temp_file.name, 0o755)
    
    try:
        start_time = time.time()
        task_func(temp_file.name, wait=False)
        end_time = time.time()
        assert (end_time - start_time) < 2  # Ensure it didn't wait
    finally:
        os.remove(temp_file.name)

def test_task_func_script_with_args():
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp_file:
        temp_file.write("#!/usr/bin/env python\nimport sys\nprint(sys.argv[1])")
        temp_file.close()
        os.chmod(temp_file.name, 0o755)
    
    try:
        return_code = task_func(temp_file.name, wait=True, "test_arg")
        assert return_code == 0
    finally:
        os.remove(temp_file.name)