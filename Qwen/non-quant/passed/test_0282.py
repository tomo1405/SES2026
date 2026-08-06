import pytest
from src_0282 import task_func
import os
from collections import Counter

def test_task_func_no_logs(tmpdir):
    # Create a temporary directory with no .log files
    folder_path = tmpdir.mkdir("test_dir")
    result = task_func(str(folder_path))
    assert result == {}

def test_task_func_single_log_with_ips(tmpdir):
    # Create a temporary directory with one .log file containing IPs
    folder_path = tmpdir.mkdir("test_dir")
    log_file = folder_path.join("test.log")
    log_file.write("192.168.1.1 some text 192.168.1.2 more text 192.168.1.1")
    result = task_func(str(folder_path))
    expected = {'192.168.1.1': 2, '192.168.1.2': 1}
    assert result == expected

def test_task_func_multiple_logs_with_ips(tmpdir):
    # Create a temporary directory with multiple .log files containing IPs
    folder_path = tmpdir.mkdir("test_dir")
    log_file1 = folder_path.join("test1.log")
    log_file1.write("192.168.1.1 some text 192.168.1.2")
    log_file2 = folder_path.join("test2.log")
    log_file2.write("192.168.1.1 more text 192.168.1.3")
    result = task_func(str(folder_path))
    expected = {'192.168.1.1': 2, '192.168.1.2': 1, '192.168.1.3': 1}
    assert result == expected

def test_task_func_logs_without_ips(tmpdir):
    # Create a temporary directory with .log files that do not contain IPs
    folder_path = tmpdir.mkdir("test_dir")
    log_file1 = folder_path.join("test1.log")
    log_file1.write("no ip here")
    log_file2 = folder_path.join("test2.log")
    log_file2.write("neither here")
    result = task_func(str(folder_path))
    assert result == {}

def test_task_func_invalid_folder_path():
    # Test with an invalid folder path
    with pytest.raises(FileNotFoundError):
        task_func("/nonexistent/path")

def test_task_func_empty_logs(tmpdir):
    # Create a temporary directory with empty .log files
    folder_path = tmpdir.mkdir("test_dir")
    log_file1 = folder_path.join("test1.log")
    log_file1.write("")
    log_file2 = folder_path.join("test2.log")
    log_file2.write("")
    result = task_func(str(folder_path))
    assert result == {}