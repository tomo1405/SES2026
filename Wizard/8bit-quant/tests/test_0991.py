python
import binascii
import base64
import urllib.parse
import codecs
import pytest

from src_0991 import task_func

def test_task_func():
    # Test with a simple string
    assert task_func("48656c6c6f20776f726c64") == {
        "hex": "48656c6c6f20776f726c64",
        "base64": "SGVsbG8gd29ybGQ=",
        "utf-8": "Hello world",
        "utf-16": "Hello world",
        "utf-32": "Hello world",
        "ASCII": "Hello world",
        "URL": "Hello%20world",
        "ROT13": "Uryyb jbeyq"
    }

    # Test with a string containing non-ASCII characters
    assert task_func("48c3a96c6c6fc3b27264") == {
        "hex": "48c3a96c6c6fc3b27264",
        "base64": "SGk/bGllIHdvcmxk",
        "utf-8": "H\xc3\xa9llo world",
        "utf-16": "H\u00e9llo world",
        "utf-32": "H\u0000\u0000\u0000\u0045llo world",
        "ASCII": "Not representable in ASCII",
        "URL": "H%C3%A9llo%20world",
        "ROT13": "Uryyb jbeyq"
    }

    # Test with an empty string
    assert task_func("") == {
        "hex": "",
        "base64": "",
        "utf-8": "",
        "utf-16": "",
        "utf-32": "",
        "ASCII": "",
        "URL": "",
        "ROT13": ""
    }