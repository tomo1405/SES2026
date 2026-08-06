import os
import random
import subprocess

from src_0746 import task_func


def test_task_func():
    script_name = random.choice(['script1.sh', 'script2.sh', 'script3.sh'])
    script_path = os.path.join('/path/to/scripts', script_name)
    subprocess.call(script_path, shell=True)
    assert task_func() == script_path