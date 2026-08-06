import pytest
from src_0786 import task_func
import os
import glob
import tempfile
import tarfile

# Mocking subprocess.run to prevent actual file operations
class MockSubprocess:
    def run(self, *args, **kwargs):
        pass

@pytest.fixture
def mock_subprocess(monkeypatch):
    monkeypatch.setattr(subprocess, 'run', MockSubprocess().run)

@pytest.fixture
def setup_files(tmp_path):
    # Create some temporary files
    test_files = []
    for i in range(3):
        file_path = tmp_path / f'testfile_{i}.txt'
        file_path.write_text(f'This is test file {i}')
        test_files.append(str(file_path))
    return test_files

def test_task_func_no_files_found():
    assert task_func('non_existent_pattern') == "No files found matching the pattern."

def test_task_func_archive_creation(setup_files, mock_subprocess):
    pattern = setup_files[0].replace('0', '*')
    result = task_func(pattern)
    
    # Check if the archive directory exists
    assert os.path.exists('/tmp/archive')

    # Check if the archive file is created
    assert os.path.isfile(result)

    # Check if the original files are deleted
    for file in setup_files:
        assert not os.path.exists(file)

    # Check if the archive contains the correct files
    with tarfile.open(result, 'r:gz') as tar:
        files_in_archive = tar.getnames()
        for file in setup_files:
            assert os.path.basename(file) in files_in_archive

def test_task_func_archive_name_uniqueness(setup_files, mock_subprocess):
    pattern = setup_files[0].replace('0', '*')
    first_archive = task_func(pattern)

    # Create more files with the same pattern
    for i in range(3, 6):
        file_path = os.path.join(os.path.dirname(setup_files[0]), f'testfile_{i}.txt')
        with open(file_path, 'w') as f:
            f.write(f'This is test file {i}')
        setup_files.append(file_path)

    second_archive = task_func(pattern)

    # Check if the archive names are unique
    assert first_archive != second_archive
    assert first_archive.endswith('.tar.gz')
    assert second_archive.endswith('_1.tar.gz')

def test_task_func_cleanup(setup_files, mock_subprocess):
    pattern = setup_files[0].replace('0', '*')
    task_func(pattern)

    # Check if the archive directory is cleaned up
    assert not os.path.exists('/tmp/archive')