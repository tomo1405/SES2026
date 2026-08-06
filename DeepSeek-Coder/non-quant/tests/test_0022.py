import pytest
from src_0022 import task_func

def test_task_func():
    result = task_func()
    assert 'OS' in result
    assert 'Architecture' in result
    assert 'Memory Usage' in result
    assert isinstance(result['OS'], str)
    assert isinstance(result['Architecture'], str)
    assert isinstance(result['Memory Usage'], str)
    assert float(result['Memory Usage'].rstrip('%')) <= 100