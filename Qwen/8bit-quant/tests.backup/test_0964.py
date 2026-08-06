import pytest
from src_0964 import task_func
import os
import zipfile
from pathlib import Path
import tempfile

def test_task_func_nonexistent_source_directory():
    with tempfile.TemporaryDirectory() as target_dir:
        with pytest.raises(OSError, match="source_directory must exist."):
            task_func("/nonexistent/source", target_dir, "test_zip")

def test_task_func_nonexistent_target_directory():
    with tempfile.TemporaryDirectory() as source_dir:
        target_dir = "/nonexistent/target"
        result = task_func(source_dir, target_dir, "test_zip")
        assert os.path.exists(result)
        assert os.path.isdir(target_dir)

def test_task_func_existing_target_directory():
    with tempfile.TemporaryDirectory() as source_dir:
        with tempfile.TemporaryDirectory() as target_dir:
            result = task_func(source_dir, target_dir, "test_zip")
            assert os.path.exists(result)
            assert os.path.isdir(target_dir)

def test_task_func_empty_source_directory():
    with tempfile.TemporaryDirectory() as source_dir:
        with tempfile.TemporaryDirectory() as target_dir:
            result = task_func(source_dir, target_dir, "test_zip")
            assert os.path.exists(result)
            with zipfile.ZipFile(result, "r") as zipf:
                assert len(zipf.namelist()) == 0

def test_task_func_with_files():
    with tempfile.TemporaryDirectory() as source_dir:
        with tempfile.TemporaryDirectory() as target_dir:
            # Create some files with supported extensions
            for ext in [".txt", ".docx", ".xlsx", ".csv"]:
                Path(source_dir, f"file{ext}").touch()
                Path(source_dir, "subdir", f"file{ext}").parent.mkdir(parents=True)
                Path(source_dir, "subdir", f"file{ext}").touch()

            result = task_func(source_dir, target_dir, "test_zip")
            assert os.path.exists(result)
            with zipfile.ZipFile(result, "r") as zipf:
                expected_files = ["file.txt", "file.docx", "file.xlsx", "file.csv",
                                "subdir/file.txt", "subdir/file.docx", "subdir/file.xlsx", "subdir/file.csv"]
                assert set(zipf.namelist()) == set(expected_files)

def test_task_func_strip_zip_name():
    with tempfile.TemporaryDirectory() as source_dir:
        with tempfile.TemporaryDirectory() as target_dir:
            Path(source_dir, "file.txt").touch()
            result = task_func(source_dir, target_dir, "  test_zip  ")
            assert os.path.basename(result) == "test_zip.zip"

def test_task_func_absolute_path():
    with tempfile.TemporaryDirectory() as source_dir:
        with tempfile.TemporaryDirectory() as target_dir:
            Path(source_dir, "file.txt").touch()
            result = task_func(source_dir, target_dir, "test_zip")
            assert os.path.isabs(result)