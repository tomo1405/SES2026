import pytest
from src_0347 import task_func
import os
import sys
import subprocess

# Mocking subprocess.Popen for testing
class MockPopen:
    def __init__(self, args, **kwargs):
        self.args = args
        self.returncode = 0
        self.stderr = b""
        self.stdout = b""

    def communicate(self):
        return self.stdout, self.stderr

    def poll(self):
        return self.returncode

@pytest.fixture
def mock_subprocess(mocker):
    mocker.patch('src_0347.subprocess.Popen', side_effect=MockPopen)

def test_task_func_script_exists(mock_subprocess, tmp_path):
    script_path = tmp_path / "test_script.py"
    script_path.write_text("#!/usr/bin/env python\nprint('Hello, World!')")
    os.chmod(script_path, 0o755)

    result = task_func(str(script_path), wait=True)
    assert result == 0

def test_task_func_script_not_exists(mock_subprocess):
    with pytest.raises(ValueError) as excinfo:
        task_func("non_existent_script.py", wait=True)
    assert str(excinfo.value) == "Script 'non_existent_script.py' does not exist."

def test_task_func_with_args(mock_subprocess, tmp_path):
    script_path = tmp_path / "test_script.py"
    script_path.write_text("#!/usr/bin/env python\nimport sys\nprint(sys.argv)")
    os.chmod(script_path, 0o755)

    result = task_func(str(script_path), wait=True, "arg1", "arg2")
    assert result == 0

def test_task_func_no_wait(mock_subprocess, tmp_path):
    script_path = tmp_path / "test_script.py"
    script_path.write_text("#!/usr/bin/env python\ntime.sleep(2)")
    os.chmod(script_path, 0o755)

    result = task_func(str(script_path), wait=False)
    assert result is None

def test_task_func_script_exception(mock_subprocess, tmp_path):
    script_path = tmp_path / "test_script.py"
    script_path.write_text("#!/usr/bin/env python\nraise Exception('Test exception')")
    os.chmod(script_path, 0o755)

    with pytest.raises(subprocess.CalledProcessError) as excinfo:
        task_func(str(script_path), wait=True)
    assert excinfo.value.returncode != 0