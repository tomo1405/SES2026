import pytest
from src_0506 import task_func

def test_task_func():
    assert task_func("secret", "message") == "a7d7d46f340e6d0a1c194e7f3f5b54b9e5d5c3d99a7e9e6e54b55b3a8c9d1d6c"