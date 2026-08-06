import pytest
from src_0027 import task_func

def test_task_func():
    message = "Hello, World!"
    encryption_key = "secret_key"
    expected_output = "gAAAAABb_wcV8N7Oc5-yLXpQn8Mu82g32RvNgYp34567890"
    assert task_func(message, encryption_key) == expected_output

def test_task_func_with_invalid_message():
    message = 1234
    encryption_key = "secret_key"
    with pytest.raises(TypeError):
        task_func(message, encryption_key)

def test_task_func_with_invalid_encryption_key():
    message = "Hello, World!"
    encryption_key = 1234
    with pytest.raises(TypeError):
        task_func(message, encryption_key)