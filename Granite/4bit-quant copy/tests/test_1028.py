import pytest
from src_1028 import task_func

def test_task_func():
    test_cases = [
        ("http://example.com/?q=42", "42"),
        ("http://example.com/?q=43", "43"),
        ("http://example.com/?q=foo", "foo"),
        ("http://example.com/?q=bar", "bar"),
    ]
    for url, expected_output in test_cases:
        output = task_func(url)
        assert output == expected_output, f"Failed for input {url}"

if __name__ == "__main__":
    pytest.main()