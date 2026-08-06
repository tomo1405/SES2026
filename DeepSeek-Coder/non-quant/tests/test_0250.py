import pytest
from src_0250 import task_func

def test_task_func():
    train_data, test_data = task_func()
    assert len(train_data) + len(test_data) == 10000
    assert len(train_data) > 0
    assert len(test_data) > 0
    assert len(train_data) + len(test_data) == 10000