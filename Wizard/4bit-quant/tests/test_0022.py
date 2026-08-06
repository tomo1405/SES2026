python
import platform
import psutil
import pytest

from src_0022 import task_func

def test_task_func():
    system_info = task_func()

    assert isinstance(system_info, dict)
    assert 'OS' in system_info
    assert 'Architecture' in system_info
    assert 'Memory Usage' in system_info

    assert isinstance(system_info['OS'], str)
    assert isinstance(system_info['Architecture'], str)
    assert isinstance(system_info['Memory Usage'], str)

    assert system_info['OS'] in ['Windows', 'Linux', 'Darwin']
    assert system_info['Architecture'] in ['64bit', '32bit']

    total_memory = psutil.virtual_memory().total
    used_memory = psutil.virtual_memory().used
    assert system_info['Memory Usage'] == f'{used_memory/total_memory*100:.2f}%'