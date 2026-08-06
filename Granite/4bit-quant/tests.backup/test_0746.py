import subprocess
import random
import os

SCRIPTS = ['script1.sh', 'script2.sh', 'script3.sh']
SCRIPTS_DIR = '/path/to/scripts'

def task_func():
    script_name = random.choice(SCRIPTS)
    script_path = os.path.join(SCRIPTS_DIR, script_name)  # Generate the full path
    subprocess.call(script_path, shell=True)

    return script_path  # Return the full path

import pytest

def test_task_func():
    # Test case 1: Test if a randomly chosen script is executed successfully
    script_name = random.choice(SCRIPTS)
    script_path = os.path.join(SCRIPTS_DIR, script_name)
    result = subprocess.call(script_path, shell=True)
    assert result == 0  # Assuming a successful execution returns 0

    # Test case 2: Test if the correct script is executed when given a specific input
    script_name = 'script2.sh'
    script_path = os.path.join(SCRIPTS_DIR, script_name)
    result = subprocess.call(script_path, shell=True)
    assert result == 0

    # Test case 3: Test if an error is raised when the input script does not exist
    script_name = 'invalid_script.sh'
    script_path = os.path.join(SCRIPTS_DIR, script_name)
    with pytest.raises(FileNotFoundError):
        subprocess.call(script_path, shell=True)