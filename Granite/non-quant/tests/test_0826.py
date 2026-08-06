import string

from src_0826 import task_func


def test_task_func():
    # Test case 1: Default arguments
    result = task_func(length=3)
    assert len(result) == 10
    for item in result:
        assert len(item) == 3
    # Test case 2: Custom arguments
    result = task_func(length=5, seed=42, alphabets=list(string.ascii_uppercase))
    assert len(result) == 10
    for item in result:
        assert len(item) == 5
    assert all(c.isupper() for c in ''.join(result))