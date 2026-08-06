import pytest
from src_0643 import task_func

def test_task_func():
    directory = "/path/to/directory"
    pattern = r"(?<!Distillr)\\AcroTray\.exe"
    expected_output = {
        "/path/to/directory/file1.exe": "<hash_value_1>",
        "/path/to/directory/file2.exe": "<hash_value_2>",
        # Add more expected output as needed
    }
    actual_output = task_func(directory, pattern)
    assert actual_output == expected_output

if __name__ == "__main__":
    pytest.main()