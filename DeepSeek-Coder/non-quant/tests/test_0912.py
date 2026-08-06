import pytest
from src_0912 import task_func

def test_task_func():
    # Test case 1: Single letter
    assert task_func('A') == 1

    # Test case 2: Multiple letters
    assert task_func('AB') == 2

    # Test case 3: Larger set of letters
    assert task_func('ABC') == 6

    # Test case 4: Edge case with a single letter
    assert task_func('Z') == 26

    print("All tests passed!")