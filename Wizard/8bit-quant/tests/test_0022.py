python
import psutil
import platform
import pytest

def task_func():
    system_info = {}

    system_info['OS'] = platform.system()
    system_info['Architecture'] = platform.architecture()[0]

    total_memory = psutil.virtual_memory().total
    used_memory = psutil.virtual_memory().used
    system_info['Memory Usage'] = f'{used_memory/total_memory*100:.2f}%'

    return system_info

def test_task_func():
    system_info = task_func()
    assert system_info['OS'] == platform.system()
    assert system_info['Architecture'] == platform.architecture()[0]
    assert system_info['Memory Usage'] == f'{used_memory/total_memory*100:.2f}%'