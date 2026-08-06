import pytest
from src_0643 import task_func
import os
import hashlib
import binascii
import re

# Mocking os.walk and os.path.join for testing
class MockWalk:
    def __init__(self, directory, files):
        self.directory = directory
        self.files = files

    def __iter__(self):
        yield (self.directory, [], self.files)

def mock_os_walk(directory, topdown=True, onerror=None, followlinks=False):
    if directory == './test_dir':
        return MockWalk('./test_dir', ['AcroTray.exe'])
    else:
        return []

def mock_os_path_join(root, file):
    return os.path.join(root, file)

@pytest.fixture(autouse=True)
def patch_os(monkeypatch):
    monkeypatch.setattr(os, 'walk', mock_os_walk)
    monkeypatch.setattr(os.path, 'join', mock_os_path_join)

def test_task_func():
    # Arrange
    directory = './test_dir'
    pattern = r"(?<!Distillr)\\AcroTray\.exe"
    expected_output = {
        './test_dir/AcroTray.exe': 'expected_hash_value'  # This should be replaced with the actual hash value
    }

    # Act
    result = task_func(directory, pattern)

    # Assert
    assert isinstance(result, dict)
    assert len(result) == 1
    assert './test_dir/AcroTray.exe' in result
    assert isinstance(result['./test_dir/AcroTray.exe'], str)

    # Verify the hash value
    with open('./test_dir/AcroTray.exe', 'rb') as f:
        data = f.read()
        hash_digest = hashlib.sha256(data).digest()
        actual_hash_value = binascii.hexlify(hash_digest).decode()
    assert result['./test_dir/AcroTray.exe'] == actual_hash_value