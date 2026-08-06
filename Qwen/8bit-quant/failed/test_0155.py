import pytest
from src_0155 import task_func
import os
import glob
import mimetypes
import tempfile

# Mocking the mimetypes.guess_type function to control its behavior
def mock_guess_type(filename):
    if filename.endswith('.txt'):
        return 'text/plain'
    elif filename.endswith('.jpg'):
        return 'image/jpeg'
    else:
        return None

mimetypes.guess_type = mock_guess_type

@pytest.fixture
def temp_dir():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create some test files
        open(os.path.join(tmpdir, 'test1.txt'), 'w').close()
        open(os.path.join(tmpdir, 'test2.jpg'), 'w').close()
        open(os.path.join(tmpdir, 'test3.pdf'), 'w').close()
        yield tmpdir

def test_task_func_with_txt_files(temp_dir):
    result = task_func(temp_dir, '*.txt', '.txt')
    expected = {
        'test1.txt': 'text/plain'
    }
    assert result == expected

def test_task_func_with_jpg_files(temp_dir):
    result = task_func(temp_dir, '*.jpg', '.jpg')
    expected = {
        'test2.jpg': 'image/jpeg'
    }
    assert result == expected

def test_task_func_with_no_matching_files(temp_dir):
    result = task_func(temp_dir, '*.png', '.png')
    expected = {}
    assert result == expected

def test_task_func_with_no_suffix_match(temp_dir):
    result = task_func(temp_dir, '*.txt', '.jpg')
    expected = {}
    assert result == expected

def test_task_func_with_empty_directory():
    with tempfile.TemporaryDirectory() as tmpdir:
        result = task_func(tmpdir, '*.txt', '.txt')
        expected = {}
        assert result == expected