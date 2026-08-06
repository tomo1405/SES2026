import os
import re
import pytest
from src_0007 import task_func

def test_task_func():
    pattern = r'pattern'
    log_dir = '/var/log/'
    log_files = [f for f in os.listdir(log_dir) if re.match(pattern, f)]
    log_files = sorted(log_files, key=lambda f: os.path.getmtime(os.path.join(log_dir, f)), reverse=True)
    expected_result = os.path.join(log_dir, log_files[0]) if log_files else None
    actual_result = task_func(pattern, log_dir)
    assert actual_result == expected_result

def test_task_func_with_no_log_files():
    pattern = r'pattern'
    log_dir = '/var/log/'
    log_files = [f for f in os.listdir(log_dir) if re.match(pattern, f)]
    expected_result = None
    actual_result = task_func(pattern, log_dir)
    assert actual_result == expected_result

def test_task_func_with_invalid_pattern():
    pattern = r'invalid_pattern'
    log_dir = '/var/log/'
    log_files = [f for f in os.listdir(log_dir) if re.match(pattern, f)]
    expected_result = None
    actual_result = task_func(pattern, log_dir)
    assert actual_result == expected_result