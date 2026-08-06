import pytest
from src_1132 import task_func

def test_task_func():
    salt = "my_salt"
    cursor = "my_cursor"
    count_updated = task_func(salt, cursor)
    assert count_updated == 1