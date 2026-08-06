import pytest
from src_0963 import task_func
from pathlib import Path
import tempfile
import shutil

def test_task_func_no_files():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        result = task_func(source_dir, target_dir)
        assert result == 0
        assert len(os.listdir(target_dir)) == 0

def test_task_func_single_file():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        source_path = Path(source_dir) / "file.txt"
        source_path.write_text("Hello, world!")
        result = task_func(source_dir, target_dir)
        assert result == 1
        assert len(os.listdir(target_dir)) == 1
        assert (Path(target_dir) / "file.txt").exists()

def test_task_func_multiple_files_same_name():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        source_path1 = Path(source_dir) / "file.txt"
        source_path2 = Path(source_dir) / "subdir" / "file.txt"
        source_path1.write_text("Hello, world!")
        source_path2.write_text("Another file!")
        os.makedirs(source_path2.parent)
        result = task_func(source_dir, target_dir)
        assert result == 2
        assert len(os.listdir(target_dir)) == 2
        assert (Path(target_dir) / "file.txt").exists()
        assert (Path(target_dir) / "file-1.txt").exists()

def test_task_func_different_extensions():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        source_paths = [
            Path(source_dir) / "file1.txt",
            Path(source_dir) / "file2.docx",
            Path(source_dir) / "file3.xlsx",
            Path(source_dir) / "file4.csv"
        ]
        for path in source_paths:
            path.write_text("Content")
        result = task_func(source_dir, target_dir)
        assert result == 4
        assert len(os.listdir(target_dir)) == 4
        for ext in [".txt", ".docx", ".xlsx", ".csv"]:
            assert (Path(target_dir) / f"file{ext}").exists()

def test_task_func_source_directory_not_exists():
    with tempfile.TemporaryDirectory() as target_dir:
        with pytest.raises(FileNotFoundError):
            task_func("nonexistent_directory", target_dir)

def test_task_func_target_directory_exists():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        source_path = Path(source_dir) / "file.txt"
        source_path.write_text("Hello, world!")
        os.makedirs(target_dir)
        result = task_func(source_dir, target_dir)
        assert result == 1
        assert len(os.listdir(target_dir)) == 1
        assert (Path(target_dir) / "file.txt").exists()