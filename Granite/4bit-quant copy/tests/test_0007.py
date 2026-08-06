import os
import re
import pytest

def task_func(pattern, log_dir='/var/log/'):
    log_files = [f for f in os.listdir(log_dir) if re.match(pattern, f)]
    log_files = sorted(log_files, key=lambda f: os.path.getmtime(os.path.join(log_dir, f)), reverse=True)

    return os.path.join(log_dir, log_files[0]) if log_files else None

def test_task_func():
    assert task_func(r'file_\d+.log', '/var/log/') == '/var/log/file_123.log'
    assert task_func(r'file_\d+.log', '/var/log/') != '/var/log/file_456.log'
    assert task_func(r'file_\d+.log', '/var/log/') is not None
    assert task_func(r'file_\d+.log', '/var/log/') is not None
    assert task_func(r'file_\d+.log', '/var/log/') is not None
    assert task_func(r'file_\d+.log', '/var/log/') is not None