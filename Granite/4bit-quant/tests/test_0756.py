import os
import glob
import pytest

def task_func(directory_path):
    new_filenames = []
    for filename in glob.glob(os.path.join(directory_path, '*')):
        base_name = os.path.basename(filename)
        new_base_name = '.'.join(base_name.split('.')[::-1])
        os.rename(filename, os.path.join(directory_path, new_base_name))
        new_filenames.append(new_base_name)
    return new_filenames

def test_task_func():
    test_directory = "test_directory"
    test_files = ["file1.txt", "file2.txt", "file3.txt"]
    for file in test_files:
        open(os.path.join(test_directory, file), 'a').close()
    expected_output = ["txt.file1", "txt.file2", "txt.file3"]
    output = task_func(test_directory)
    assert output == expected_output
    for file in test_files:
        os.remove(os.path.join(test_directory, file))

if __name__ == "__main__":
    pytest.main()