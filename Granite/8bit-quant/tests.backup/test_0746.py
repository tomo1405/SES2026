import subprocess
import random
import os
import pytest
from src_0746 import task_func

def test_task_func():
    script_name = random.choice(SCRIPTS)
    script_path = os.path.join(SCRIPTS_DIR, script_name)
    with patch('subprocess.call') as mock_call:
        task_func()
        mock_call.assert_called_with(script_path, shell=True)

def test_task_func_random_script():
    with patch('random.choice') as mock_choice:
        mock_choice.return_value = 'script2.sh'
        script_path = task_func()
        assert script_path == os.path.join(SCRIPTS_DIR, 'script2.sh')