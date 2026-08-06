import re
import os
import shutil
import pytest

def task_func(directory):
    pattern = re.compile(r'(like|what)', re.IGNORECASE)
    interesting_files = [file for file in os.listdir(directory) if pattern.search(file)]

    if not os.path.exists(os.path.join(directory, 'Interesting Files')):
        os.mkdir(os.path.join(directory, 'Interesting Files'))

    for file in interesting_files:
        shutil.move(os.path.join(directory, file), os.path.join(directory, 'Interesting Files'))

    return interesting_files

def test_task_func():
    test_directory = "/path/to/test/directory"
    test_files = ["file1.txt", "file2.txt", "file3.txt"]
    for file in test_files:
        with open(os.path.join(test_directory, file), "w") as f:
            f.write("Test file content")

    expected_interesting_files = ["file1.txt", "file2.txt", "file3.txt"]
    actual_interesting_files = task_func(test_directory)
    assert actual_interesting_files == expected_interesting_files, "interesting_files should contain all files that match the pattern"
    assert os.path.exists(os.path.join(test_directory, 'Interesting Files')), "Interesting Files directory should be created"
    for file in test_files:
        assert os.path.exists(os.path.join(test_directory, 'Interesting Files', file)), f"File {file} should be moved to Interesting Files directory"

if __name__ == "__main__":
    pytest.main()