import pytest
from src_0778 import task_func
import os
import tempfile
import zipfile

def create_test_zip_file(directory, base_name, number):
    zip_path = os.path.join(directory, f"{base_name}-{number}.zip")
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        zipf.writestr(f"file_{number}.txt", "This is a test file.")
    return zip_path

def create_test_directory():
    temp_dir = tempfile.mkdtemp()
    create_test_zip_file(temp_dir, "test_base", 1)
    create_test_zip_file(temp_dir, "test_base", 2)
    create_test_zip_file(temp_dir, "other_base", 3)
    return temp_dir

def remove_test_directory(temp_dir):
    for root, dirs, files in os.walk(temp_dir, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(temp_dir)

def test_task_func():
    temp_dir = create_test_directory()
    try:
        result = task_func(temp_dir)
        assert len(result) == 2
        assert os.path.exists(os.path.join(temp_dir, "test_base"))
        assert os.path.exists(os.path.join(temp_dir, "other_base"))
        assert not os.path.exists(os.path.join(temp_dir, "test_base-1"))
        assert not os.path.exists(os.path.join(temp_dir, "test_base-2"))
        assert not os.path.exists(os.path.join(temp_dir, "other_base-3"))
    finally:
        remove_test_directory(temp_dir)

def test_task_func_no_matches():
    temp_dir = tempfile.mkdtemp()
    try:
        result = task_func(temp_dir)
        assert len(result) == 0
    finally:
        os.rmdir(temp_dir)

def test_task_func_empty_directory():
    temp_dir = tempfile.mkdtemp()
    try:
        result = task_func(temp_dir)
        assert len(result) == 0
    finally:
        os.rmdir(temp_dir)

def test_task_func_with_custom_pattern():
    temp_dir = create_test_directory()
    try:
        custom_pattern = r'^(.*?)-\d+\.zip$'
        result = task_func(temp_dir, pattern=custom_pattern)
        assert len(result) == 2
        assert os.path.exists(os.path.join(temp_dir, "test_base"))
        assert os.path.exists(os.path.join(temp_dir, "other_base"))
    finally:
        remove_test_directory(temp_dir)