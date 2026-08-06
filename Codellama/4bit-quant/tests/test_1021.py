import pytest
from src_1021 import task_func

def test_task_func():
    # Test with default arguments
    data = task_func()
    assert isinstance(data, dict)

    # Test with custom arguments
    data = task_func(from_encoding="utf8", to_encoding="utf8")
    assert isinstance(data, dict)

    # Test with invalid arguments
    with pytest.raises(ValueError):
        task_func(from_encoding="invalid")

    with pytest.raises(ValueError):
        task_func(to_encoding="invalid")

    # Test with empty content
    data = task_func(from_encoding=None, to_encoding="utf8")
    assert data == {}

    # Test with non-empty content
    data = task_func(from_encoding=None, to_encoding="utf8")
    assert isinstance(data, dict)

    # Test with invalid content
    with pytest.raises(ValueError):
        task_func(from_encoding=None, to_encoding="invalid")

    with pytest.raises(ValueError):
        task_func(from_encoding="invalid", to_encoding="invalid")