import re
import os
import glob
import mimetypes
from src_0155 import task_func

def test_task_func():
    directory = "/path/to/directory"
    file_pattern = "*.txt"
    suffix = r".*\.txt$"
    expected_output = {
        "file1.txt": "text/plain",
        "file2.txt": "text/plain",
        "file3.txt": "text/plain"
    }
    os.chdir(directory)
    files = glob.glob(file_pattern)
    for file in files:
        if re.search(suffix, file):
            file_type = mimetypes.guess_type(file)[0]
            expected_output[file] = file_type
    actual_output = task_func(directory, file_pattern, suffix)
    assert actual_output == expected_output