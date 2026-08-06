python
import subprocess
import os
import threading
import pytest

from src_1105 import task_func

def test_task_func():
    script_path = 'script.py'
    timeout = 60

    def target():
        subprocess.call(['python', script_path])

    thread = threading.Thread(target=target)
    thread.start()

    thread.join(timeout)

    if thread.is_alive():
        os.system(f'pkill -f "{script_path}"')
        thread.join()
        assert task_func(script_path, timeout) == 'Terminating process due to timeout.'
    else:
        assert task_func(script_path, timeout) == 'Script executed successfully.'