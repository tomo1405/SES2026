import pytest
from src_1051 import task_func
import os
import hashlib
import tempfile

def test_task_func():
    # Create a temporary directory to use as the DIRECTORY constant
    temp_dir = tempfile.mkdtemp()

    # Monkeypatch the DIRECTORY constant to use the temporary directory
    old_directory = task_func.DIRECTORY
    task_func.DIRECTORY = temp_dir

    try:
        # Test case: Single line input
        input_string = "hello world"
        expected_hash = hashlib.sha256(input_string.encode()).hexdigest()
        expected_filename = expected_hash[:10] + ".txt"
        expected_filepath = os.path.join(temp_dir, expected_filename)
        expected_file_paths = [expected_filepath]

        assert task_func(input_string) == expected_file_paths
        assert os.path.exists(expected_filepath)
        with open(expected_filepath, "r", encoding="utf-8") as file:
            assert file.read() == expected_hash

        # Test case: Multiple lines input
        input_string = "hello world\nanother line\n"
        expected_hashes = [
            hashlib.sha256("hello world".encode()).hexdigest(),
            hashlib.sha256("another line".encode()).hexdigest()
        ]
        expected_filenames = [
            expected_hashes[0][:10] + ".txt",
            expected_hashes[1][:10] + ".txt"
        ]
        expected_filepaths = [
            os.path.join(temp_dir, expected_filenames[0]),
            os.path.join(temp_dir, expected_filenames[1])
        ]
        expected_file_paths.extend(expected_filepaths)

        assert task_func(input_string) == expected_file_paths
        for hash_value, filepath in zip(expected_hashes, expected_filepaths):
            assert os.path.exists(filepath)
            with open(filepath, "r", encoding="utf-8") as file:
                assert file.read() == hash_value

        # Test case: Empty input string
        input_string = ""
        assert task_func(input_string) == []

        # Test case: Input string with only newline characters
        input_string = "\n\n\n"
        assert task_func(input_string) == []

    finally:
        # Clean up: Remove the temporary directory and restore the original DIRECTORY constant
        task_func.DIRECTORY = old_directory
        os.rmdir(temp_dir)