python
import subprocess
import os
import time
from datetime import datetime

def task_func(script_dir, scripts, delay):
    if delay < 0:
        raise ValueError("delay cannot be negative.")
    if not scripts:
        raise ValueError("No scripts provided.")
    start_times = []
    for script in scripts:
        script_path = os.path.join(script_dir, script)
        start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        start_times.append(start_time)

        result = subprocess.call(script_path, shell=True)
        if result != 0:
            raise FileNotFoundError(f"Script not found: {script_path}")

        time.sleep(delay)
    return start_times

def test_task_func():
    script_dir = "path/to/scripts"
    scripts = ["script1.sh", "script2.sh"]
    delay = 10

    start_times = task_func(script_dir, scripts, delay)

    assert len(start_times) == len(scripts)
    for start_time in start_times:
        assert isinstance(start_time, str)