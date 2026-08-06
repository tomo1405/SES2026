import pytest
from src_0032 import task_func

def test_task_func():
    text = "This is a sample text. It contains $10 and $20."
    result = task_func(text)
    assert result is not None
    assert isinstance(result, object)
    assert result.get_geometry() == (10, 5)