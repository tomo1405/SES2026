import pytest
from src_0991 import task_func

def test_task_func():
    hex_string = "48656c6c6f20576f726c64"  # "Hello World" in hex
    expected_output = {
        "hex": "48656c6c6f20576f726c64",
        "base64": "SGVsbG8gV29ybGQ=",
        "utf-8": "Hello World",
        "utf-16": "Hello World",
        "utf-32": "Hello World",
        "ASCII": "Hello World",
        "URL": "Hello%20World",
        "ROT13": "Uryyb Jbeyq"
    }
    assert task_func(hex_string) == expected_output

def test_task_func_non_ascii():
    hex_string = "c3a9206c61206d656c616e6365"  # "é la mélancie" in hex
    expected_output = {
        "hex": "c3a9206c61206d656c616e6365",
        "base64": "w6kgbGEgbWVsYW5jaWU=",
        "utf-8": "é la mélancie",
        "utf-16": "é la mélancie",
        "utf-32": "é la mélancie",
        "ASCII": "Not representable in ASCII",
        "URL": "%C3%A9%20la%20m%C3%A9lancie",
        "ROT13": "r y nyr zravatrq"
    }
    assert task_func(hex_string) == expected_output

def test_task_func_empty_string():
    hex_string = ""
    expected_output = {
        "hex": "",
        "base64": "",
        "utf-8": "",
        "utf-16": "",
        "utf-32": "",
        "ASCII": "",
        "URL": "",
        "ROT13": ""
    }
    assert task_func(hex_string) == expected_output