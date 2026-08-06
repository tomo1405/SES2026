import subprocess
import time
import threading
from src_0325 import task_func

def test_task_func():
    file_list = ['file1.txt', 'file2.txt', 'file3.txt']
    expected_exit_codes = [0, 1, 0]

    exit_codes = task_func(file_list)

    assert exit_codes == expected_exit_codes

def test_task_func_with_empty_file_list():
    file_list = []
    expected_exit_codes = []

    exit_codes = task_func(file_list)

    assert exit_codes == expected_exit_codes