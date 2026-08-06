import pytest
from src_0786 import task_func
import os
import glob
import tempfile

# Constants
ARCHIVE_DIR = '/tmp/archive'

@pytest.fixture(autouse=True)
def cleanup():
    """Cleanup the archive directory after each test."""
    if os.path.exists(ARCHIVE_DIR):
        for file in os.listdir(ARCHIVE_DIR):
            os.remove(os.path.join(ARCHIVE_DIR, file))
        os.rmdir(ARCHIVE_DIR)

def test_no_files_found():
    """Test case where no files match the pattern."""
    result = task_func('nonexistent_pattern*')
    assert result == "No files found matching the pattern."

def test_archive_creation():
    """Test case where files match the pattern and archive is created."""
    # Create temporary files
    with tempfile.TemporaryDirectory() as temp_dir:
        file1 = os.path.join(temp_dir, 'testfile1.txt')
        file2 = os.path.join(temp_dir, 'testfile2.txt')
        with open(file1, 'w') as f:
            f.write('content1')
        with open(file2, 'w') as f:
            f.write('content2')

        # Call the function with a pattern that matches the created files
        pattern = os.path.join(temp_dir, 'testfile*.txt')
        result = task_func(pattern)

        # Check if the archive file exists
        assert os.path.exists(result)
        assert result.startswith(os.path.join(ARCHIVE_DIR, 'archive'))

        # Check if the original files are deleted
        assert not os.path.exists(file1)
        assert not os.path.exists(file2)

def test_archive_with_existing_name():
    """Test case where an archive file with the same name already exists."""
    # Create a mock archive file with the same base name
    archive_file_base = os.path.join(ARCHIVE_DIR, 'archive')
    archive_file = archive_file_base + '.tar.gz'
    with open(archive_file, 'w') as f:
        f.write('existing archive content')

    # Create temporary files
    with tempfile.TemporaryDirectory() as temp_dir:
        file1 = os.path.join(temp_dir, 'testfile1.txt')
        with open(file1, 'w') as f:
            f.write('content1')

        # Call the function with a pattern that matches the created file
        pattern = os.path.join(temp_dir, 'testfile*.txt')
        result = task_func(pattern)

        # Check if the archive file with a new suffix exists
        assert os.path.exists(result)
        assert result.startswith(os.path.join(ARCHIVE_DIR, 'archive_'))
        assert result.endswith('.tar.gz')

        # Check if the original file is deleted
        assert not os.path.exists(file1)