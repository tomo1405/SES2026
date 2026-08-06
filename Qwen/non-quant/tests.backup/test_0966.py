import pytest
from src_0966 import task_func
import os
import tempfile
import shutil

def test_task_func_no_source_directory():
    with tempfile.TemporaryDirectory() as target_dir:
        result = task_func("non_existent_source", target_dir)
        assert result == 0

def test_task_func_empty_source_directory():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        result = task_func(source_dir, target_dir)
        assert result == 0

def test_task_func_no_target_directory():
    with tempfile.TemporaryDirectory() as source_dir:
        result = task_func(source_dir, "non_existent_target")
        assert result == 0

def test_task_func_move_files_with_pattern():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        # Create some files in the source directory
        files_to_create = ["file1.txt", "file2023.docx", "file3.pdf", "file4000.jpg"]
        for file in files_to_create:
            open(os.path.join(source_dir, file), 'a').close()

        # Call the function
        result = task_func(source_dir, target_dir, pattern=r"\d{4}")

        # Check that only files matching the pattern were moved
        assert result == 2
        assert set(os.listdir(target_dir)) == {"file2023.docx", "file4000.jpg"}
        assert set(os.listdir(source_dir)) == {"file1.txt", "file3.pdf"}

def test_task_func_no_files_match_pattern():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        # Create some files in the source directory
        files_to_create = ["file1.txt", "file2.docx", "file3.pdf", "file4.jpg"]
        for file in files_to_create:
            open(os.path.join(source_dir, file), 'a').close()

        # Call the function
        result = task_func(source_dir, target_dir, pattern=r"\d{4}")

        # Check that no files were moved
        assert result == 0
        assert set(os.listdir(target_dir)) == set()
        assert set(os.listdir(source_dir)) == set(files_to_create)

def test_task_func_with_subdirectories():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        # Create subdirectories and files in the source directory
        subdirs = ["subdir1", "subdir2/subsubdir"]
        for subdir in subdirs:
            os.makedirs(os.path.join(source_dir, subdir))
        
        files_to_create = [
            ("subdir1", "file1.txt"),
            ("subdir1", "file2023.docx"),
            ("subdir2/subsubdir", "file3.pdf"),
            ("subdir2/subsubdir", "file4000.jpg")
        ]
        for subdir, file in files_to_create:
            open(os.path.join(source_dir, subdir, file), 'a').close()

        # Call the function
        result = task_func(source_dir, target_dir, pattern=r"\d{4}")

        # Check that only files matching the pattern were moved
        assert result == 2
        assert set(os.listdir(target_dir)) == {"file2023.docx", "file4000.jpg"}
        for subdir, file in files_to_create:
            if file not in {"file2023.docx", "file4000.jpg"}:
                assert os.path.exists(os.path.join(source_dir, subdir, file))