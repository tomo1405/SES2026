import json
import os
import pytest

def task_func(file_path):
    if not os.path.exists(file_path):
        return False

    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            return False

    return isinstance(data, list) and all(isinstance(item, dict) for item in data)

def test_task_func():
    test_cases = [
        ("/path/to/valid/file.json", True),
        ("/path/to/invalid/file.json", False),
        ("/path/to/another/invalid/file.json", False),
    ]

    for file_path, expected_output in test_cases:
        result = task_func(file_path)
        assert result == expected_output, f"Failed for file path: {file_path}"

if __name__ == "__main__":
    pytest.main()