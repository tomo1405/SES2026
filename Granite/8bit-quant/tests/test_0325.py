import subprocess
import time
import threading
from src_0325 import task_func

def test_task_func():
    file_list = ["file1.txt", "file2.txt", "file3.txt"]
    exit_codes = task_func(file_list)
    assert len(exit_codes) == len(file_list)
    for exit_code in exit_codes:
        assert exit_code is not None

def test_task_func_with_empty_file_list():
    file_list = []
    exit_codes = task_func(file_list)
    assert len(exit_codes) == 0

def test_task_func_with_none_file_list():
    file_list = None
    exit_codes = task_func(file_list)
    assert len(exit_codes) == 0