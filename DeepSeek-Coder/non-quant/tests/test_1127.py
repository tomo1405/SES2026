import pytest
from src_1127 import task_func

def test_task_func():
    assert task_func("Hello, World!") == "a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e"
    assert task_func("Python3.8") == "79b4e4d5e6e1d1630e6b4e09f8c4a9b46d79b4b4d6e659c2d0bae4d8d8d5b14a"
    assert task_func("12345") == "8d969eef6ecad3c29a3a6292834baddc98ef617e1ad8b45e66c2e74a8f9e511e8"
    assert task_func("!@#$%^&*()") == "5e2e93f5f8c6e5b8d4c7d2bde5a9d3e9e6e6c1f83f8a8b59a6f35a143e361e66"