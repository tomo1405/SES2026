import pytest
from src_0462 import task_func
import os
import tempfile
import subprocess

def test_task_func_nonexistent_script():
    with pytest.raises(FileNotFoundError):
        task_func("nonexistent_script.sh")

def test_task_func_valid_script():
    # Create a temporary script file
    script_content = "#!/bin/bash\nsleep 1"
    with tempfile.NamedTemporaryFile(delete=False, suffix=".sh") as temp_file:
        temp_file.write(script_content.encode())
        temp_file.flush()
        os.chmod(temp_file.name, 0o755)

        # Run the function
        result = task_func(temp_file.name, timeout=5)

        # Clean up the temporary file
        os.unlink(temp_file.name)

        # Check that the result is a dictionary with expected keys
        assert isinstance(result, dict)
        assert "CPU Usage" in result
        assert "Memory Usage" in result

def test_task_func_timeout():
    # Create a temporary script file that sleeps longer than the timeout
    script_content = "#!/bin/bash\nsleep 10"
    with tempfile.NamedTemporaryFile(delete=False, suffix=".sh") as temp_file:
        temp_file.write(script_content.encode())
        temp_file.flush()
        os.chmod(temp_file.name, 0o755)

        # Run the function with a short timeout
        result = task_func(temp_file.name, timeout=1)

        # Clean up the temporary file
        os.unlink(temp_file.name)

        # Check that the result is a dictionary with expected keys
        assert isinstance(result, dict)
        assert "CPU Usage" in result
        assert "Memory Usage" in result

def test_task_func_no_process():
    # Create a temporary script file that exits immediately
    script_content = "#!/bin/bash\necho 'Hello'"
    with tempfile.NamedTemporaryFile(delete=False, suffix=".sh") as temp_file:
        temp_file.write(script_content.encode())
        temp_file.flush()
        os.chmod(temp_file.name, 0o755)

        # Run the function
        result = task_func(temp_file.name, timeout=5)

        # Clean up the temporary file
        os.unlink(temp_file.name)

        # Check that the result is a dictionary with expected keys
        assert isinstance(result, dict)
        assert "CPU Usage" in result
        assert "Memory Usage" in result