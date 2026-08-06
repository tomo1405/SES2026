import pytest
from src_0007 import task_func

def test_task_func():
    pattern = r'^error\.log$'
    log_dir = '/var/log/'
    log_files = [f for f in os.listdir(log_dir) if re.match(pattern, f)]
    log_files = sorted(log_files, key=lambda f: os.path.getmtime(os.path.join(log_dir, f)), reverse=True)

    assert task_func(pattern, log_dir) == os.path.join(log_dir, log_files[0])

def test_task_func_no_match():
    pattern = r'^error\.log$'
    log_dir = '/var/log/'
    log_files = [f for f in os.listdir(log_dir) if re.match(pattern, f)]
    log_files = sorted(log_files, key=lambda f: os.path.getmtime(os.path.join(log_dir, f)), reverse=True)

    assert task_func(pattern, log_dir) == None