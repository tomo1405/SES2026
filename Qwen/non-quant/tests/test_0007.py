import pytest
from src_0007 import task_func
import os
import tempfile
import datetime

@pytest.fixture
def temp_log_dir():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create some mock log files
        for i in range(3):
            file_path = os.path.join(tmpdir, f"log_file_{i}.log")
            with open(file_path, 'w') as f:
                f.write("Mock log content")
            # Set different modification times
            os.utime(file_path, (datetime.datetime.now().timestamp(), datetime.datetime.now().timestamp() - i))
        yield tmpdir

def test_task_func_with_existing_logs(temp_log_dir):
    pattern = r"log_file_\d+\.log"
    result = task_func(pattern, log_dir=temp_log_dir)
    assert result == os.path.join(temp_log_dir, "log_file_2.log")

def test_task_func_with_no_matching_logs(temp_log_dir):
    pattern = r"nonexistent_pattern\.log"
    result = task_func(pattern, log_dir=temp_log_dir)
    assert result is None

def test_task_func_with_empty_directory():
    with tempfile.TemporaryDirectory() as tmpdir:
        pattern = r"log_file_\d+\.log"
        result = task_func(pattern, log_dir=tmpdir)
        assert result is None

def test_task_func_with_non_existent_directory():
    pattern = r"log_file_\d+\.log"
    with pytest.raises(FileNotFoundError):
        task_func(pattern, log_dir="/non_existent_directory/")