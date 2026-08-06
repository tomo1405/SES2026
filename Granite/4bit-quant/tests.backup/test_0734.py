import re
import string
from src_0734 import task_func

def test_task_func():
    assert task_func("This is a test.") == 2
    assert task_func("This is a test, right?") == 2
    assert task_func("This is a test! Is it working?") == 4
    assert task_func("This is a test! Is it working? Let's check.") == 6
    assert task_func("This is a test! Is it working? Let's check. This is a test.") == 6
    assert task_func("This is a test! Is it working? Let's check. This is a test. Yes, it is.") == 8