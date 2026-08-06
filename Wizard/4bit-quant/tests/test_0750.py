python
import pytest
from src_0750 import task_func

def test_task_func():
    myList = [1, 2, 3, 4, 5]
    expected_result = [0.0, 0.25, 0.5, 0.75, 1.0]
    result = task_func(myList)
    assert result == expected_result