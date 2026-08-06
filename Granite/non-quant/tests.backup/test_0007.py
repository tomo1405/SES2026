import os
import re
import pytest
from src_0007 import task_func

def test_task_func():
    # Test case 1: pattern matches a file in log_dir
    pattern = r'pattern1.*'
    log_dir = '/var/log/'
    expected_result = '/var/log/pattern1.log'
    assert task_func(pattern, log_dir) == expected_result

    # Test case 2: pattern does not match any file in log_dir
    pattern = r'pattern2.*'
    log_dir = '/var/log/'
    expected_result = None
    assert task_func(pattern, log_dir) == expected_result

    # Test case 3: log_dir is empty
    pattern = r'.*'
    log_dir = '/var/log/'
    expected_result = None
    assert task_func(pattern, log_dir) == expected_result

    # Test case 4: pattern matches multiple files in log_dir
    pattern = r'.*'
    log_dir = '/var/log/'
    expected_result = '/var/log/pattern3.log'
    assert task_func(pattern, log_dir) == expected_result