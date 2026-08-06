import pytest
from src_0997 import task_func

def test_task_func():
    # Test case 1: Basic functionality
    url = "https://example.com"
    file_name = "test_output.txt"
    result = task_func(url, file_name)
    assert result == file_name
    with open(file_name, "r", encoding="utf-8") as f:
        content = f.read().strip()
        assert json.loads(content)["title"] == "None"

    # Add more test cases as needed