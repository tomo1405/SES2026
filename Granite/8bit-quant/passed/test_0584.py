import pytest
from src_0584 import task_func

def test_task_func():
    pub_key, filename, password, nonce = task_func()
    assert pub_key  # Check if pub_key is not None
    assert filename  # Check if filename is not None
    assert password  # Check if password is not None
    assert nonce  # Check if nonce is not None