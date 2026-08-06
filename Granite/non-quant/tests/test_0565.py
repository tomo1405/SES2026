import pytest
from src_0565 import task_func

def test_task_func():
    filepath = 'path/to/file'
    lib_name, metadata = task_func(filepath)
    assert lib_name is not None
    assert isinstance(metadata, dict)
    assert 'Creation Time' in metadata
    assert 'Modification Time' in metadata
    assert 'Size' in metadata