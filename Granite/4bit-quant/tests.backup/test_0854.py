import os
import shutil
import string
from src_0854 import task_func

INVALID_CHARACTERS = string.punctuation + string.whitespace

def test_task_func():
    test_cases = [
        (
            "test_directory",
            ["file1.txt", "file2.png", "file3.exe", "file4.txt", "file5.png"],
            {
                "txt": 2,
                "png": 2,
                "exe": 1
            }
        ),
        (
            "test_directory",
            ["file1.txt", "file2.png", "file3.exe", "file4.txt", "file5.png", "file6.invalid"],
            {
                "txt": 2,
                "png": 2,
                "exe": 1,
                "invalid": 1
            }
        )
    ]

    for directory, files, expected_summary in test_cases:
        with open(os.path.join(directory, "test_file.txt"), "w") as f:
            f.write("Test file content")

        for file in files:
            with open(os.path.join(directory, file), "w") as f:
                f.write("Test file content")

        summary = task_func(directory)
        assert summary == expected_summary, f"Summary for directory {directory} does not match expected summary"

        shutil.rmtree(directory)

test_task_func()