import re
import os
import glob
import pytest

def task_func(dir_path: str) -> list:
    new_names = []
    for file_path in glob.glob(os.path.join(dir_path, '*')):
        base_name = os.path.basename(file_path)
        new_name = re.sub('[^A-Za-z0-9]+', '', base_name)
        new_path = os.path.join(dir_path, new_name)
        os.rename(file_path, new_path)
        new_names.append(new_name)
    return new_names

def test_task_func():
    test_dir = "/path/to/test/directory"
    test_files = ["file1.txt", "file2.txt", "file3.txt"]
    for file in test_files:
        open(os.path.join(test_dir, file), 'a').close()
    expected_output = ["file1", "file2", "file3"]
    actual_output = task_func(test_dir)
    assert actual_output == expected_output, "Output does not match expected output"
    for file in test_files:
        os.remove(os.path.join(test_dir, file))

if __name__ == "__main__":
    pytest.main()