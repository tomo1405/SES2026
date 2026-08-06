import os
from datetime import datetime
import pytest

def task_func(filepath: str) -> dict:
    try:
        size = os.path.getsize(filepath)
        mtime = os.path.getmtime(filepath)
        mtime = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S')
    except OSError as e:
        raise Exception(f"Error: {e}")

    return {'size': f"{size} bytes", 'last_modified': mtime}

def test_task_func():
    test_cases = [
        ("/path/to/file1.txt", {'size': '123 bytes', 'last_modified': '2023-01-01 12:00:00'}),
        ("/path/to/file2.txt", {'size': '456 bytes', 'last_modified': '2023-01-02 13:00:00'})
    ]

    for filepath, expected_output in test_cases:
        actual_output = task_func(filepath)
        assert actual_output == expected_output, f"Failed for filepath: {filepath}"

if __name__ == "__main__":
    pytest.main()