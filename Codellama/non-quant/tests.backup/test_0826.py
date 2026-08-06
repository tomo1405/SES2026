import pytest
from src_0826 import task_func

def test_task_func():
    # Test with default arguments
    result = task_func(length=5)
    assert len(result) == 10
    assert all(len(x) == 5 for x in result)
    assert all(x in string.ascii_lowercase for x in result)

    # Test with custom arguments
    result = task_func(length=5, seed=42, alphabets=list(string.ascii_uppercase))
    assert len(result) == 10
    assert all(len(x) == 5 for x in result)
    assert all(x in string.ascii_uppercase for x in result)

    # Test with invalid arguments
    with pytest.raises(ValueError):
        task_func(length=0)
    with pytest.raises(ValueError):
        task_func(length=-1)
    with pytest.raises(ValueError):
        task_func(length=1.5)
    with pytest.raises(ValueError):
        task_func(length="abc")
    with pytest.raises(ValueError):
        task_func(length=None)
    with pytest.raises(ValueError):
        task_func(seed="abc")
    with pytest.raises(ValueError):
        task_func(alphabets="abc")
    with pytest.raises(ValueError):
        task_func(alphabets=None)