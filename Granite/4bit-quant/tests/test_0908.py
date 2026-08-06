import os
import re
import pytest

def task_func(pattern: str, replacement: str, directory: str) -> bool:
    try:
        for file in os.listdir(directory):
            if re.search(pattern, file):
                new_filename = re.sub(pattern, replacement, file)
                os.rename(os.path.join(directory, file), os.path.join(directory, new_filename))
        return True
    except Exception as e:
        return False

def test_task_func():
    # Test case 1: successful file renaming
    directory = "/path/to/directory"
    pattern = r"^old_prefix_"
    replacement = "new_prefix_"
    expected_result = True
    actual_result = task_func(pattern, replacement, directory)
    assert actual_result == expected_result

    # Test case 2: failed file renaming due to exception
    directory = "/path/to/invalid_directory"
    pattern = r"^old_prefix_"
    replacement = "new_prefix_"
    expected_result = False
    actual_result = task_func(pattern, replacement, directory)
    assert actual_result == expected_result

    # Test case 3: successful file renaming with multiple files
    directory = "/path/to/directory"
    pattern = r"^old_prefix_"
    replacement = "new_prefix_"
    for i in range(10):
        filename = f"old_prefix_{i}.txt"
        with open(os.path.join(directory, filename), "w") as f:
            f.write("Test content")
    expected_result = True
    actual_result = task_func(pattern, replacement, directory)
    assert actual_result == expected_result

if __name__ == "__main__":
    pytest.main()