python
import subprocess
import psutil
import time
import os

from src_0462 import task_func

def test_task_func():
    # Test case 1: script file does not exist
    with pytest.raises(FileNotFoundError):
        task_func("non_existent_script.sh")

    # Test case 2: script file exists, but does not run successfully
    script_path = "script.sh"
    with open(script_path, "w") as f:
        f.write("exit 1")
    with pytest.raises(subprocess.CalledProcessError):
        task_func(script_path)

    # Test case 3: script file exists and runs successfully
    script_path = "script.sh"
    with open(script_path, "w") as f:
        f.write("echo 'Hello, World!'")
    result = task_func(script_path)
    assert result["CPU Usage"] == 0.0
    assert result["Memory Usage"] > 0

    # Test case 4: script file exists and runs successfully, but times out
    script_path = "script.sh"
    with open(script_path, "w") as f:
        f.write("while true; do echo 'Hello, World!'; sleep 1; done")
    result = task_func(script_path, timeout=1)
    assert result["CPU Usage"] > 0
    assert result["Memory Usage"] > 0