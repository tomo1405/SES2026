import pytest
from src_1125 import task_func

def test_task_func():
    test_cases = [
        ("https://www.example.com", "Example Domain"),
        ("https://www.google.com", "Google"),
        ("https://www.github.com", "GitHub"),
    ]
    for url, expected_title in test_cases:
        result = task_func(url)
        assert result == expected_title, f"Failed for URL: {url}"

if __name__ == "__main__":
    pytest.main()