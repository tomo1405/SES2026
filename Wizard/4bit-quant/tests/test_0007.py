python
import os
import re
import pytest

from src_0007 import task_func

def test_task_func():
    pattern = '.*\.log$'
    log_dir = '/var/log/'
    expected_result = '/var/log/app.log'

    # Test case 1: Valid pattern and log directory
    result = task_func(pattern, log_dir)
    assert result == expected_result

    # Test case 2: Invalid pattern
    pattern = '.*\.txt$'
    result = task_func(pattern, log_dir)
    assert result is None

    # Test case 3: Invalid log directory
    log_dir = '/var/logs/'
    result = task_func(pattern, log_dir)
    assert result is None

    # Test case 4: Empty log directory
    log_dir = '/var/empty/'
    result = task_func(pattern, log_dir)
    assert result is None

    # Test case 5: Empty pattern
    pattern = ''
    result = task_func(pattern, log_dir)
    assert result is None

    # Test case 6: Invalid pattern and log directory
    pattern = '.*\.txt$'
    log_dir = '/var/logs/'
    result = task_func(pattern, log_dir)
    assert result is None