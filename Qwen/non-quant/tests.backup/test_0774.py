import pytest
from src_0774 import task_func
import os
import shutil
import tempfile

# Mocking os and shutil modules for testing
class MockOs:
    def __init__(self):
        self.listdir_calls = []
        self.listdir_return_values = []

    def listdir(self, path):
        self.listdir_calls.append(path)
        return self.listdir_return_values.pop(0)

class MockShutil:
    def __init__(self):
        self.move_calls = []

    def move(self, src, dst):
        self.move_calls.append((src, dst))

@pytest.fixture
def mock_os(monkeypatch):
    mock_os = MockOs()
    monkeypatch.setattr(os, 'listdir', mock_os.listdir)
    return mock_os

@pytest.fixture
def mock_shutil(monkeypatch):
    mock_shutil = MockShutil()
    monkeypatch.setattr(shutil, 'move', mock_shutil.move)
    return mock_shutil

@pytest.fixture
def setup_directories():
    source_dir = tempfile.mkdtemp()
    target_dir = tempfile.mkdtemp()
    yield source_dir, target_dir
    shutil.rmtree(source_dir)
    shutil.rmtree(target_dir)

def test_task_func(mock_os, mock_shutil, setup_directories):
    source_dir, target_dir = setup_directories

    # Create some test files in the source directory
    with open(os.path.join(source_dir, 'file-1.json'), 'w') as f:
        f.write('{"key": "value"}')
    with open(os.path.join(source_dir, 'file-2.json'), 'w') as f:
        f.write('{"key": "value"}')
    with open(os.path.join(source_dir, 'other-file.txt'), 'w') as f:
        f.write('Some text')

    # Configure the mock os.listdir to return the created files
    mock_os.listdir_return_values.append(['file-1.json', 'file-2.json', 'other-file.txt'])

    # Call the function
    task_func()

    # Assert that os.listdir was called with the correct source directory
    assert mock_os.listdir_calls == [SOURCE_DIR]

    # Assert that shutil.move was called with the correct arguments
    expected_move_calls = [
        (os.path.join(SOURCE_DIR, 'file-1.json'), os.path.join(TARGET_DIR, 'file.json')),
        (os.path.join(SOURCE_DIR, 'file-2.json'), os.path.join(TARGET_DIR, 'file.json'))
    ]
    assert mock_shutil.move_calls == expected_move_calls

    # Check that the files were moved correctly
    assert not os.path.exists(os.path.join(source_dir, 'file-1.json'))
    assert not os.path.exists(os.path.join(source_dir, 'file-2.json'))
    assert os.path.exists(os.path.join(target_dir, 'file.json'))