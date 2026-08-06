python
import base64
import re
from html import unescape
import textwrap

def task_func(raw_string, line_length):

    # Decode the string from base64
    decoded_string = base64.b64decode(raw_string).decode('utf-8')

    # Unescape HTML entities
    unescaped_string = unescape(decoded_string)

    # Replace multiple spaces with a single space and strip leading and trailing spaces
    cleaned_string = re.sub(' +', ' ', unescaped_string).strip()

    # Wrap the text
    wrapped_text = textwrap.fill(cleaned_string, line_length)

    return wrapped_text

def test_task_func():
    # Test case 1
    assert task_func('VGhpcyBpcyBhIHRlc3Q=', 10) == 'This is a test'

    # Test case 2
    assert task_func('SG93IHRvIHlvdXIgZGVzaWdu', 15) == 'Some text here'

    # Test case 3
    assert task_func('VGhpcyBpcyB0aGUgZGVzaWduYXR1cmUgYW5kIGJ1dHRvbiB0aGF0IHdhcyB0aGUgY2xvdWQu', 20) == 'This is the best day to come here'