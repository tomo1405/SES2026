python
import os
import re
import pytest

def task_func(pattern, log_dir='/var/log/'):
    log_files = [f for f in os.listdir(log_dir) if re.match(pattern, f)]
    log_files = sorted(log_files, key=lambda f: os.path.getmtime(os.path.join(log_dir, f)), reverse=True)

    return os.path.join(log_dir, log_files[0]) if log_files else None

def test_task_func():
    assert task_func('.*\.log$') == '/var/log/test.log'
    assert task_func('.*\.txt$') == '/var/log/test.txt'
    assert task_func('.*\.log$', log_dir='/var/log/apache2/') == '/var/log/apache2/access.log'
    assert task_func('.*\.txt$', log_dir='/var/log/apache2/') == None