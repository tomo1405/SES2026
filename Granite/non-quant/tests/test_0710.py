import base64
import re
from html import unescape
import textwrap
from src_0710 import task_func
import pytest

@pytest.mark.parametrize("raw_string, line_length, expected_output", [
    (b"SGVsbG8gV29ybGQh", 10, "Hello World!"),
    (b"SGVsbG8gV29ybGQh", 20, "Hello World!"),
    (b"SGVsbG8gV29ybGQh", 1, "H\ne\nl\nl\no\n \nW\no\nr\nl\nd\n!"),
])
def test_task_func(raw_string, line_length, expected_output):
    decoded_string = base64.b64decode(raw_string).decode('utf-8')
    unescaped_string = unescape(decoded_string)
    cleaned_string = re.sub(' +', ' ', unescaped_string).strip()
    wrapped_text = textwrap.fill(cleaned_string, line_length)
    assert wrapped_text == expected_output