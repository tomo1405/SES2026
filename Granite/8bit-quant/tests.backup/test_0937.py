import pytest
from src_0937 import task_func

def test_task_func():
    with pytest.raises(ValueError):
        task_func('hello123')
    with pytest.raises(ValueError):
        task_func('HELLO')
    with pytest.raises(ValueError):
        task_func('123')
    assert task_func('hello').get_xlabel() == 'Letter Index'
    assert task_func('hello').get_ylabel() == 'Alphabetical Position'
    assert task_func('hello').get_title() == 'Alphabetical Position of Letters in Word'