import textwrap
import re
import pytest

def task_func(input_string, width):
    lines = input_string.split('\\n')
    wrapped_lines = [textwrap.fill(line, width, break_long_words=False) for line in lines]
    wrapped_string = '\\n'.join(wrapped_lines)
    wrapped_string = re.sub(r'\bis\b', 'was', wrapped_string)
    return wrapped_string

def test_task_func():
    input_string = "This is a test string\nwith multiple lines."
    width = 20
    expected_output = "This was a test string\nwith multiple lines."
    actual_output = task_func(input_string, width)
    assert actual_output == expected_output, "Output does not match expected output"

if __name__ == "__main__":
    pytest.main()