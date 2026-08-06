import pytest
from src_0963 import task_func
import os
from pathlib import Path
import shutil

# Mocking functions and paths for testing
class MockPath:
    def __init__(self, path):
        self.path = path

    def exists(self):
        return self.path in mock_exists

    def mkdirs(self, *args, **kwargs):
        mock_makedirs.append(self.path)

    def name(self):
        return os.path.basename(self.path)

    def stem(self):
        return os.path.splitext(os.path.basename(self.path))[0]

def mock_glob(pattern, recursive):
    return mock_globs.get(pattern, [])

# Mock variables
mock_exists = []
mock_makedirs = []
mock_globs = {}

@pytest.fixture
def setup_mock():
    global mock_exists, mock_makedirs, mock_globs
    mock_exists = []
    mock_makedirs = []
    mock_globs = {}

@pytest.fixture
def create_temp_directories(tmp_path):
    source_dir = tmp_path / "source"
    target_dir = tmp_path / "target"
    source_dir.mkdir()
    return source_dir, target_dir

def test_task_func_source_not_exist(create_temp_directories):
    source_dir, target_dir = create_temp_directories
    with pytest.raises(FileNotFoundError):
        task_func(str(source_dir), str(target_dir))

def test_task_func_target_not_exist(create_temp_directories):
    source_dir, target_dir = create_temp_directories
    mock_exists.append(str(source_dir))
    moved_files = task_func(str(source_dir), str(target_dir))
    assert moved_files == 0
    assert str(target_dir) in mock_makedirs

def test_task_func_no_files(create_temp_directories):
    source_dir, target_dir = create_temp_directories
    mock_exists.append(str(source_dir))
    mock_exists.append(str(target_dir))
    moved_files = task_func(str(source_dir), str(target_dir))
    assert moved_files == 0

def test_task_func_move_files(create_temp_directories):
    source_dir, target_dir = create_temp_directories
    mock_exists.append(str(source_dir))
    mock_exists.append(str(target_dir))
    mock_globs[os.path.join(str(source_dir), "**", "*.txt")] = [
        str(source_dir / "file1.txt"),
        str(source_dir / "subdir" / "file2.txt")
    ]
    mock_globs[os.path.join(str(source_dir), "**", "*.docx")] = [
        str(source_dir / "file3.docx")
    ]

    moved_files = task_func(str(source_dir), str(target_dir))
    assert moved_files == 3
    assert (target_dir / "file1.txt").exists()
    assert (target_dir / "file2.txt").exists()
    assert (target_dir / "file3.docx").exists()

def test_task_func_handle_conflict(create_temp_directories):
    source_dir, target_dir = create_temp_directories
    mock_exists.append(str(source_dir))
    mock_exists.append(str(target_dir))
    mock_globs[os.path.join(str(source_dir), "**", "*.txt")] = [
        str(source_dir / "file1.txt"),
        str(source_dir / "file1.txt")
    ]

    moved_files = task_func(str(source_dir), str(target_dir))
    assert moved_files == 2
    assert (target_dir / "file1.txt").exists()
    assert (target_dir / "file1-1.txt").exists()

def test_task_func_multiple_extensions(create_temp_directories):
    source_dir, target_dir = create_temp_directories
    mock_exists.append(str(source_dir))
    mock_exists.append(str(target_dir))
    mock_globs[os.path.join(str(source_dir), "**", "*.txt")] = [
        str(source_dir / "file1.txt")
    ]
    mock_globs[os.path.join(str(source_dir), "**", "*.docx")] = [
        str(source_dir / "file2.docx")
    ]
    mock_globs[os.path.join(str(source_dir), "**", "*.xlsx")] = [
        str(source_dir / "file3.xlsx")
    ]
    mock_globs[os.path.join(str(source_dir), "**", "*.csv")] = [
        str(source_dir / "file4.csv")
    ]

    moved_files = task_func(str(source_dir), str(target_dir))
    assert moved_files == 4
    assert (target_dir / "file1.txt").exists()
    assert (target_dir / "file2.docx").exists()
    assert (target_dir / "file3.xlsx").exists()
    assert (target_dir / "file4.csv").exists()