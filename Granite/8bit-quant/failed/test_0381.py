import re
import os
import shutil
import pytest

def task_func(directory):
    for filename in os.listdir(directory):
        match = re.search(r'\.(.*?)$', filename)
        if match:
            ext_dir = os.path.join(directory, match.group(1))
            if not os.path.exists(ext_dir):
                os.mkdir(ext_dir)
            shutil.move(os.path.join(directory, filename), ext_dir)

def test_task_func():
    test_dir = "test_directory"
    test_filename = "test_file.txt"
    test_ext_dir = os.path.join(test_dir, "txt")
    os.makedirs(test_ext_dir, exist_ok=True)
    with open(os.path.join(test_dir, test_filename), "w") as f:
        f.write("Test file content")
    task_func(test_dir)
    assert os.path.exists(test_ext_dir)
    assert os.path.exists(os.path.join(test_ext_dir, test_filename))
    os.remove(os.path.join(test_dir, test_filename))
    os.rmdir(test_ext_dir)
    os.rmdir(test_dir)