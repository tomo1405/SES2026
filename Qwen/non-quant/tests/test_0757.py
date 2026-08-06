import pytest
from src_0757 import task_func
from pathlib import Path
import shutil
import tempfile

@pytest.fixture
def setup_directories():
    source_dir = tempfile.mkdtemp()
    target_dir = tempfile.mkdtemp()
    yield source_dir, target_dir
    shutil.rmtree(source_dir)
    shutil.rmtree(target_dir)

@pytest.fixture
def create_files(source_dir):
    files = [
        ("file1.txt", "txt"),
        ("file2.docx", "docx"),
        ("file3.txt", "txt"),
        ("file4.pdf", "pdf"),
    ]
    for file_name, _ in files:
        Path(source_dir) / file_name
    return [file_name for file_name, _ in files]

def test_task_func_with_valid_input(setup_directories, create_files):
    source_dir, target_dir = setup_directories
    for file_name in create_files:
        (Path(source_dir) / file_name).touch()

    result = task_func(source_dir, target_dir, [".txt", ".docx"])

    assert result == 3
    assert not any((Path(source_dir) / file_name).exists() for file_name in create_files)
    assert all((Path(target_dir) / file_name).exists() for file_name in create_files if file_name.endswith((".txt", ".docx")))

def test_task_func_with_nonexistent_source_dir(setup_directories):
    _, target_dir = setup_directories
    with pytest.raises(ValueError, match="source_dir does not exist."):
        task_func("nonexistent_source", target_dir, [".txt"])

def test_task_func_with_nonexistent_target_dir(setup_directories):
    source_dir, _ = setup_directories
    with pytest.raises(ValueError, match="target_dir does not exist."):
        task_func(source_dir, "nonexistent_target", [".txt"])

def test_task_func_with_no_matching_files(setup_directories):
    source_dir, target_dir = setup_directories
    (Path(source_dir) / "file1.pdf").touch()

    result = task_func(source_dir, target_dir, [".txt", ".docx"])

    assert result == 0
    assert (Path(source_dir) / "file1.pdf").exists()
    assert not (Path(target_dir) / "file1.pdf").exists()

def test_task_func_with_empty_extensions(setup_directories):
    source_dir, target_dir = setup_directories
    (Path(source_dir) / "file1.txt").touch()

    result = task_func(source_dir, target_dir, [])

    assert result == 0
    assert (Path(source_dir) / "file1.txt").exists()
    assert not (Path(target_dir) / "file1.txt").exists()