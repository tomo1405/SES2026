import pytest
from src_0273 import task_func

def test_task_func():
    request_handler = task_func()
    assert request_handler.do_POST() == None