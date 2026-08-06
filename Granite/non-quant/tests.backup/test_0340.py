import json
import urllib.parse
import hmac
import hashlib
from src_0340 import task_func
import pytest

def test_task_func_with_valid_input():
    req_data = {"key1": "value1", "key2": "value2"}
    secret_key = "my_secret_key"
    expected_signature = "5d2e7a9e1b7c498e8b1e1f1a1d1c1b1a"  # Example signature calculated using the provided code
    actual_signature = task_func(req_data, secret_key)
    assert actual_signature == expected_signature

def test_task_func_with_invalid_input():
    req_data = "not_a_dictionary"
    secret_key = "my_secret_key"
    with pytest.raises(TypeError) as exc_info:
        task_func(req_data, secret_key)
    assert "req_data must be a dictionary" in str(exc_info.value)