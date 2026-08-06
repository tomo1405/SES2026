import pytest
from src_0022 import task_func

def test_task_func():
    system_info = task_func()
    assert system_info['OS'] == platform.system()
    assert system_info['Architecture'] == platform.architecture()[0]
    total_memory = psutil.virtual_memory().total
    used_memory = psutil.virtual_memory().used
    assert system_info['Memory Usage'] == f'{used_memory/total_memory*100:.2f}%'