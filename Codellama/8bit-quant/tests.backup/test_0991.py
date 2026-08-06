import pytest
from src_0991 import task_func

def test_task_func():
    hex_string = "48656c6c6f20576f726c6421"
    expected_encodings = {
        "hex": "48656c6c6f20576f726c6421",
        "base64": "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t",
        "utf-8": "Hello World!",
        "utf-16": "Hello World!",
        "utf-32": "Hello World!",
        "ASCII": "Not representable in ASCII",
        "URL": "Hello+World%21",
        "ROT13": "Uryyb+Jbeyq%21"
    }
    assert task_func(hex_string) == expected_encodings