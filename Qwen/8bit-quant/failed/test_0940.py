import pytest
from src_0940 import task_func
import os
import glob
import tempfile

def test_task_func():
    # Create a temporary directory and some files with special characters
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create test files
        test_files = [
            "file1@name.txt",
            "file2#name.doc",
            "file3$name.pdf",
            "file4 name.jpg"
        ]
        for file_name in test_files:
            with open(os.path.join(temp_dir, file_name), 'w') as f:
                f.write("Test content")

        # Expected new names after processing
        expected_new_names = [
            "file1name.txt",
            "file2name.doc",
            "file3name.pdf",
            "file4name.jpg"
        ]

        # Run the function
        new_names = task_func(temp_dir)

        # Check if the new names match the expected names
        assert sorted(new_names) == sorted(expected_new_names)

        # Check if the files have been renamed correctly
        for expected_name in expected_new_names:
            assert os.path.exists(os.path.join(temp_dir, expected_name))

        # Check if the original files no longer exist
        for original_name in test_files:
            assert not os.path.exists(os.path.join(temp_dir, original_name))