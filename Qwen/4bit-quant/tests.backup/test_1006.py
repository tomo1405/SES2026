import pytest
from src_1006 import task_func
import os
import tempfile

def test_task_func_valid_url():
    with tempfile.TemporaryDirectory() as temp_dir:
        url = "http://example.com/sample.zip"
        save_path = os.path.join(temp_dir, "downloaded_file.zip")
        extract_path = os.path.join(temp_dir, "extracted_files")
        
        result = task_func(url, save_path, extract_path)
        
        assert result == extract_path
        assert os.path.exists(extract_path)
        assert not os.path.exists(save_path)

def test_task_func_invalid_url():
    with tempfile.TemporaryDirectory() as temp_dir:
        url = "http://nonexistenturl.com/sample.zip"
        save_path = os.path.join(temp_dir, "downloaded_file.zip")
        extract_path = os.path.join(temp_dir, "extracted_files")
        
        result = task_func(url, save_path, extract_path)
        
        assert result.startswith("URL Error:")

def test_task_func_existing_save_path():
    with tempfile.TemporaryDirectory() as temp_dir:
        url = "http://example.com/sample.zip"
        save_path = os.path.join(temp_dir, "downloaded_file.zip")
        extract_path = os.path.join(temp_dir, "extracted_files")
        
        # Create an existing file at save_path
        with open(save_path, 'w') as f:
            f.write("dummy content")
        
        result = task_func(url, save_path, extract_path)
        
        assert result == extract_path
        assert os.path.exists(extract_path)
        assert not os.path.exists(save_path)

def test_task_func_extract_path_exists():
    with tempfile.TemporaryDirectory() as temp_dir:
        url = "http://example.com/sample.zip"
        save_path = os.path.join(temp_dir, "downloaded_file.zip")
        extract_path = os.path.join(temp_dir, "extracted_files")
        
        # Create the extraction directory
        os.makedirs(extract_path)
        
        result = task_func(url, save_path, extract_path)
        
        assert result == extract_path
        assert os.path.exists(extract_path)
        assert not os.path.exists(save_path)