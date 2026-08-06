import binascii
import hashlib
import os
import shutil
import tempfile

import pytest
from src_0643 import task_func


@pytest.fixture
def temp_dir():
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    shutil.rmtree(temp_dir)

def test_task_func_no_files(temp_dir):
    result = task_func(temp_dir)
    assert result == {}

def test_task_func_single_file(temp_dir):
    file_path = os.path.join(temp_dir, "AcroTray.exe")
    with open(file_path, 'wb') as f:
        f.write(b'some binary data')
    
    expected_hash = hashlib.sha256(b'some binary data').digest()
    expected_result = {file_path: binascii.hexlify(expected_hash).decode()}
    
    result = task_func(temp_dir)
    assert result == expected_result

def test_task_func_multiple_files(temp_dir):
    file1_path = os.path.join(temp_dir, "AcroTray.exe")
    file2_path = os.path.join(temp_dir, "DistillrAcroTray.exe")
    with open(file1_path, 'wb') as f:
        f.write(b'some binary data')
    with open(file2_path, 'wb') as f:
        f.write(b'different binary data')
    
    expected_hash1 = hashlib.sha256(b'some binary data').digest()
    expected_hash2 = hashlib.sha256(b'different binary data').digest()
    expected_result = {
        file1_path: binascii.hexlify(expected_hash1).decode(),
        file2_path: binascii.hexlify(expected_hash2).decode()
    }
    
    result = task_func(temp_dir)
    assert result == expected_result

def test_task_func_subdirectories(temp_dir):
    sub_dir = os.path.join(temp_dir, "subdir")
    os.makedirs(sub_dir)
    file_path = os.path.join(sub_dir, "AcroTray.exe")
    with open(file_path, 'wb') as f:
        f.write(b'some binary data')
    
    expected_hash = hashlib.sha256(b'some binary data').digest()
    expected_result = {file_path: binascii.hexlify(expected_hash).decode()}
    
    result = task_func(temp_dir)
    assert result == expected_result

def test_task_func_pattern_match(temp_dir):
    file_path = os.path.join(temp_dir, "AcroTray.exe")
    with open(file_path, 'wb') as f:
        f.write(b'some binary data')
    
    expected_hash = hashlib.sha256(b'some binary data').digest()
    expected_result = {file_path: binascii.hexlify(expected_hash).decode()}
    
    result = task_func(temp_dir, pattern=r"AcroTray\.exe")
    assert result == expected_result

def test_task_func_pattern_no_match(temp_dir):
    file_path = os.path.join(temp_dir, "AcroTray.exe")
    with open(file_path, 'wb') as f:
        f.write(b'some binary data')
    
    result = task_func(temp_dir, pattern=r"NonMatchingPattern")
    assert result == {}

def test_task_func_distillr_prefix(temp_dir):
    file_path = os.path.join(temp_dir, "DistillrAcroTray.exe")
    with open(file_path, 'wb') as f:
        f.write(b'some binary data')
    
    result = task_func(temp_dir)
    assert result == {}