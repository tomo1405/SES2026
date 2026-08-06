import pytest
from src_0552 import task_func

def test_task_func():
    assert task_func([["apple"], ["banana"], ["apple", "banana"]]) is not None
    assert task_func([["apple"], ["banana"], ["apple", "banana"]]) != None
    assert task_func([["apple"], ["banana"], ["apple", "banana"]]) != "No items to plot."
    assert task_func([[]]) == "No items to plot."
    assert task_func([]) == "No items to plot."