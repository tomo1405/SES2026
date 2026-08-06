import pytest
from src_0963 import task_func
from pathlib import Path
import os

@pytest.fixture
def setup_directories(tmp_path):
    source_dir = tmp_path / "source"
    target_dir = tmp_path / "target"
    source_dir.mkdir()
    target_dir.mkdir()

    # Create some test files
    (source_dir / "file1.txt").touch()
    (source_dir / "file2.docx").touch()
    (source_dir / "file3.xlsx").touch()
    (source_dir / "file4.csv").touch()

    return source_dir, target_dir

def test_task_func(setup_directories):
    source_dir, target_dir = setup_directories

    # Call the function
    moved_files = task_func(str(source_dir), str(target_dir))

    # Check that all files have been moved
    assert moved_files == 4
    assert not list(source_dir.iterdir())
    assert len(list(target_dir.iterdir())) == 4

def test_task_func_with_existing_target_files(setup_directories):
    source_dir, target_dir = setup_directories

    # Create a file with the same name in the target directory
    (target_dir / "file1.txt").touch()

    # Call the function
    moved_files = task_func(str(source_dir), str(target_dir))

    # Check that all files have been moved, and the conflicting file has been renamed
    assert moved_files == 4
    assert not list(source_dir.iterdir())
    assert len(list(target_dir.iterdir())) == 5
    assert any(f.name.startswith("file1-") and f.name.endswith(".txt") for f in target_dir.iterdir())

def test_task_func_nonexistent_source_directory():
    with pytest.raises(FileNotFoundError, match="source_directory must exist"):
        task_func("/nonexistent/source", "/target")

def test_task_func_nonexistent_target_directory(tmp_path):
    source_dir = tmp_path / "source"
    source_dir.mkdir()

    # Call the function
    moved_files = task_func(str(source_dir), str(tmp_path / "nonexistent_target"))

    # Check that the target directory was created and files were moved
    assert moved_files == 0
    assert (tmp_path / "nonexistent_target").exists()
    assert not list(source_dir.iterdir())