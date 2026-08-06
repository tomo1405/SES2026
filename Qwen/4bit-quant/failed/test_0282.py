import pytest
from src_0282 import task_func
import os
from collections import Counter

def test_task_func_no_logs(tmpdir):
    # Create a temporary directory with no log files
    tmpdir.mkdir("test_dir")
    result = task_func(str(tmpdir))
    assert result == {}

def test_task_func_single_log_with_ips(tmpdir):
    # Create a temporary directory with one log file containing IPs
    log_file = tmpdir.mkdir("test_dir").join("test.log")
    log_file.write("192.168.1.1 10.0.0.1 192.168.1.1")
    result = task_func(str(tmpdir.join("test_dir")))
    expected = {'192.168.1.1': 2, '10.0.0.1': 1}
    assert result == expected

def test_task_func_multiple_logs_with_ips(tmpdir):
    # Create a temporary directory with multiple log files containing IPs
    log_file1 = tmpdir.mkdir("test_dir").join("test1.log")
    log_file1.write("192.168.1.1 10.0.0.1")
    log_file2 = tmpdir.mkdir("test_dir").join("test2.log")
    log_file2.write("192.168.1.1 172.16.0.1")
    result = task_func(str(tmpdir.join("test_dir")))
    expected = {'192.168.1.1': 2, '10.0.0.1': 1, '172.16.0.1': 1}
    assert result == expected

def test_task_func_invalid_ip_format(tmpdir):
    # Create a temporary directory with a log file containing invalid IP format
    log_file = tmpdir.mkdir("test_dir").join("test.log")
    log_file.write("256.256.256.256 10.0.0.1")
    result = task_func(str(tmpdir.join("test_dir")))
    expected = {'10.0.0.1': 1}
    assert result == expected

def test_task_func_non_log_files(tmpdir):
    # Create a temporary directory with non-log files
    tmpdir.mkdir("test_dir").join("test.txt").write("This is a text file.")
    result = task_func(str(tmpdir.join("test_dir")))
    assert result == {}