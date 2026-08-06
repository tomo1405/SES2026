import pytest
from src_0329 import task_func

def test_task_func():
    assert task_func(5) == collections.OrderedDict([('Team 5', 50), ('Team 4', 40), ('Team 3', 30), ('Team 2', 20), ('Team 1', 10)])
    assert task_func(3) == collections.OrderedDict([('Team 3', 30), ('Team 2', 20), ('Team 1', 10)])
    assert task_func(1) == collections.OrderedDict([('Team 1', 10)])