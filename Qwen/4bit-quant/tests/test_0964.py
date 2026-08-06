import os
import tempfile
import zipfile

import pytest
from src_0964 import task_func


def test_task_func_valid_source_and_target():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        # Create some sample files in the source directory
        for ext in [".txt", ".docx", ".xlsx", ".csv"]:
            open(os.path.join(source_dir, f"file{ext}"), 'a').close()

        zip_name = "test_zip"
        result = task_func(source_dir, target_dir, zip_name)

        assert os.path.exists(result)
        assert result.endswith(".zip")

def test_task_func_nonexistent_source_directory():
    with tempfile.TemporaryDirectory() as target_dir:
        zip_name = "test_zip"
        with pytest.raises(OSError) as excinfo:
            task_func("nonexistent_dir", target_dir, zip_name)
        assert str(excinfo.value) == "source_directory must exist."

def test_task_func_empty_source_directory():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        zip_name = "test_zip"
        result = task_func(source_dir, target_dir, zip_name)

        assert os.path.exists(result)
        assert result.endswith(".zip")
        with zipfile.ZipFile(result, "r") as zipf:
            assert len(zipf.namelist()) == 0

def test_task_func_existing_target_directory():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        # Create some sample files in the source directory
        for ext in [".txt", ".docx", ".xlsx", ".csv"]:
            open(os.path.join(source_dir, f"file{ext}"), 'a').close()

        zip_name = "test_zip"
        result1 = task_func(source_dir, target_dir, zip_name)
        result2 = task_func(source_dir, target_dir, zip_name)

        assert os.path.exists(result1)
        assert os.path.exists(result2)
        assert result1 != result2

def test_task_func_with_whitespace_in_zip_name():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        # Create some sample files in the source directory
        for ext in [".txt", ".docx", ".xlsx", ".csv"]:
            open(os.path.join(source_dir, f"file{ext}"), 'a').close()

        zip_name = " test zip "
        result = task_func(source_dir, target_dir, zip_name)

        assert os.path.exists(result)
        assert result.endswith(".zip")
        assert os.path.basename(result) == "test_zip.zip"

def test_task_func_with_special_characters_in_zip_name():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        # Create some sample files in the source directory
        for ext in [".txt", ".docx", ".xlsx", ".csv"]:
            open(os.path.join(source_dir, f"file{ext}"), 'a').close()

        zip_name = "test@zip#name$"
        result = task_func(source_dir, target_dir, zip_name)

        assert os.path.exists(result)
        assert result.endswith(".zip")
        assert os.path.basename(result) == "test@zip#name$.zip"