import pytest
from src_0991 import task_func

def test_task_func():
    hex_string = "48656c6c6f20576f726c64"  # "Hello World" in hex
    expected_encodings = {
        "hex": "48656c6c6f20576f726c64",
        "base64": "SGVsbG8gV29ybGQ=",
        "utf-8": "Hello World",
        "utf-16": "Hello World",
        "utf-32": "Hello World",
        "ASCII": "Hello World",
        "URL": "Hello+World",
        "ROT13": "Uryyb%20Jbeyq",
    }

    encodings = task_func(hex_string)

    assert encodings == expected_encodings