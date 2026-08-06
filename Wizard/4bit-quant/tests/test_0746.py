python
import subprocess
import random
import os
import pytest

# Constants
SCRIPTS = ['script1.sh', 'script2.sh', 'script3.sh']
SCRIPTS_DIR = '/path/to/scripts'

def task_func():
    script_name = random.choice(SCRIPTS)
    script_path = os.path.join(SCRIPTS_DIR, script_name)  # Generate the full path
    subprocess.call(script_path, shell=True)

    return script_path  # Return the full path

def test_task_func():
    script_path = task_func()
    assert os.path.exists(script_path)  # Check if the script exists
    assert os.path.isfile(script_path)  # Check if the script is a file