import pytest
from src_0710 import task_func

def test_task_func_base64_decoding():
    raw_string = "SGVsbG8gV29ybGQh"  # Base64 encoding of "Hello World!"
    expected_output = "Hello World!"
    assert task_func(raw_string, 20) == expected_output

def test_task_func_html_unescaping():
    raw_string = "SGVsbG8gPGI+V29ybGQhPC9iPg=="  # Base64 encoding of "Hello <b>World!</b>"
    expected_output = "Hello World!"
    assert task_func(raw_string, 20) == expected_output

def test_task_func_multiple_spaces():
    raw_string = "SGVsbG8gICAgV29ybGQh"  # Base64 encoding of "Hello   World!"
    expected_output = "Hello World!"
    assert task_func(raw_string, 20) == expected_output

def test_task_func_leading_trailing_spaces():
    raw_string = "ICAgSGVsbG8gV29ybGQhICAg"  # Base64 encoding of "   Hello World!   "
    expected_output = "Hello World!"
    assert task_func(raw_string, 20) == expected_output

def test_task_func_text_wrapping():
    raw_string = "SGVsbG8gV29ybGQhIEkgd2FzIGluIGEgdGVzdC4="  # Base64 encoding of "Hello World! I was in a test."
    expected_output = "Hello World! I was\nin a test."
    assert task_func(raw_string, 20) == expected_output

def test_task_func_empty_string():
    raw_string = ""  # Base64 encoding of ""
    expected_output = ""
    assert task_func(raw_string, 20) == expected_output

def test_task_func_special_characters():
    raw_string = "SGVsbG8gV29ybGQhIEkgd2FzIG4pbiBzcGVjaWFsIGNvbXBseQ=="  # Base64 encoding of "Hello World! I was n'in spécial"
    expected_output = "Hello World! I was\nn'in spécial"
    assert task_func(raw_string, 20) == expected_output