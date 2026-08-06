import pytest
from src_0022 import task_func

def test_task_func():
    system_info = task_func()
    assert 'OS' in system_info
    assert 'Architecture' in system_info
    assert 'Memory Usage' in system_info
    assert isinstance(system_info['Memory Usage'], str)
    assert system_info['Memory Usage'].endswith('%')