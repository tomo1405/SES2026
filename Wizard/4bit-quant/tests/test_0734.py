python
import re
import string
import pytest

from src_0734 import task_func

def test_task_func():
    content = "This is a sample text. It contains some stop words like me, my, and myself."
    expected_count = 4

    result = task_func(content)

    assert result == expected_count