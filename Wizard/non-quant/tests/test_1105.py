python
import subprocess
import os
import threading
import pytest

def task_func(script_path: str, timeout: int = 60) -> str:
    def target():
        subprocess.call(['python', script_path])

    thread = threading.Thread(target=target)
    thread.start()

    thread.join(timeout)

    if thread.is_alive():
        os.system(f'pkill -f "{script_path}"')
        thread.join()
        return 'Terminating process due to timeout.'
    else:
        return 'Script executed successfully.'

def test_task_func():
    # Test case 1: Valid script path
    assert task_func('test.py') == 'Script executed successfully.'

    # Test case 2: Invalid script path
    with pytest.raises(FileNotFoundError):
        task_func('invalid.py')

    # Test case 3: Timeout
    assert task_func('test.py', timeout=1) == 'Terminating process due to timeout.'