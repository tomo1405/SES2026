import base64
import re
from html import unescape
import textwrap
import pytest

def task_func(raw_string, line_length):
    decoded_string = base64.b64decode(raw_string).decode('utf-8')
    unescaped_string = unescape(decoded_string)
    cleaned_string = re.sub(' +', ' ', unescaped_string).strip()
    wrapped_text = textwrap.fill(cleaned_string, line_length)
    return wrapped_text

def test_task_func():
    raw_string = "SGVsbG8gV29ybGQh"
    line_length = 10
    expected_output = "Hello World!"
    actual_output = task_func(raw_string, line_length)
    assert actual_output == expected_output

test_task_func()