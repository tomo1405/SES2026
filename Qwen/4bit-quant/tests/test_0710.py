import base64

from src_0710 import task_func


def test_task_func():
    # Test with a simple base64 encoded string
    raw_string = base64.b64encode("Hello & World!").decode('utf-8')
    line_length = 20
    expected_output = "Hello & World!"
    assert task_func(raw_string, line_length) == expected_output

    # Test with multiple spaces and HTML entities
    raw_string = base64.b64encode("   Hello &amp; &lt;World&gt;   ").decode('utf-8')
    line_length = 20
    expected_output = "Hello & World!"
    assert task_func(raw_string, line_length) == expected_output

    # Test with line wrapping
    raw_string = base64.b64encode("This is a long string that needs to be wrapped").decode('utf-8')
    line_length = 10
    expected_output = "This is a\nlong string\nthat needs\nto be\nwrapped"
    assert task_func(raw_string, line_length) == expected_output

    # Test with empty string
    raw_string = base64.b64encode("").decode('utf-8')
    line_length = 20
    expected_output = ""
    assert task_func(raw_string, line_length) == expected_output

    # Test with special characters
    raw_string = base64.b64encode("!!!Hello &amp; World!!!").decode('utf-8')
    line_length = 20
    expected_output = "!!!Hello & World!!!"
    assert task_func(raw_string, line_length) == expected_output