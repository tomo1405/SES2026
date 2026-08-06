python
import os
import binascii
import hashlib
import re
import pytest

from src_0643 import task_func

@pytest.fixture
def directory():
    return './tests/data'

def test_task_func(directory):
    hashes = task_func(directory)
    assert len(hashes) == 1
    assert list(hashes.keys())[0] == os.path.join(directory, 'subdir1', 'AcroTray.exe')
    assert hashes[os.path.join(directory, 'subdir1', 'AcroTray.exe')] == 'a7a1d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5'

def test_task_func_with_pattern(directory):
    hashes = task_func(directory, pattern=r"AcroTray\.exe")
    assert len(hashes) == 1
    assert list(hashes.keys())[0] == os.path.join(directory, 'subdir1', 'AcroTray.exe')
    assert hashes[os.path.join(directory, 'subdir1', 'AcroTray.exe')] == 'a7a1d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5'

def test_task_func_with_invalid_pattern(directory):
    hashes = task_func(directory, pattern=r"invalid_pattern")
    assert len(hashes) == 0