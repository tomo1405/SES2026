import pytest
from src_0991 import task_func

def test_task_func():
    # Test with a simple hex string
    hex_string = "68656c6c6f2c20776f726c6421"
    expected_encodings = {
        "hex": "68656c6c6f2c20776f726c6421",
        "base64": "aGVsbG8gd29ybGQh",
        "utf-8": "hello, world!",
        "utf-16": "hello, world!",
        "utf-32": "hello, world!",
        "ASCII": "Not representable in ASCII",
        "URL": "hello%2C%20world%21",
        "ROT13": "uryyb%20jbeyq%20gjragl"
    }
    assert task_func(hex_string) == expected_encodings

    # Test with a hex string that contains non-ASCII characters
    hex_string = "68656c6c6f2c20776f726c642120e28090"
    expected_encodings = {
        "hex": "68656c6c6f2c20776f726c642120e28090",
        "base64": "aGVsbG8gd29ybGQh20e28090",
        "utf-8": "hello, world! ☃",
        "utf-16": "hello, world! ☃",
        "utf-32": "hello, world! ☃",
        "ASCII": "Not representable in ASCII",
        "URL": "hello%2C%20world%21%20%E2%80%90",
        "ROT13": "uryyb%20jbeyq%20gjragl%20%E2%80%90"
    }
    assert task_func(hex_string) == expected_encodings

    # Test with a hex string that contains invalid characters
    hex_string = "68656c6c6f2c20776f726c642120invalid"
    expected_encodings = {
        "hex": "68656c6c6f2c20776f726c642120invalid",
        "base64": "aGVsbG8gd29ybGQh20invalid",
        "utf-8": "hello, world! invalid",
        "utf-16": "hello, world! invalid",
        "utf-32": "hello, world! invalid",
        "ASCII": "Not representable in ASCII",
        "URL": "hello%2C%20world%21%20invalid",
        "ROT13": "uryyb%20jbeyq%20gjragl%20invalid"
    }
    assert task_func(hex_string) == expected_encodings