import subprocess
import time
import threading
from src_0325 import task_func

def test_task_func():
    file_list = ['file1.txt', 'file2.txt', 'file3.txt']
    exit_codes = task_func(file_list)
    assert len(exit_codes) == len(file_list)
    for exit_code in exit_codes:
        assert exit_code is not None