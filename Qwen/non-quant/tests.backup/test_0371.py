import pytest
from src_0371 import task_func
import os
import json
import tempfile
import shutil

def create_temp_directory_with_json_files():
    temp_dir = tempfile.mkdtemp()
    json_files = [
        {"file1.json": '{"key1": "value1"}'},
        {"file2.json": '{"key2": "value2 with \"quotes\""}'}
    ]
    
    for filename, content in json_files:
        file_path = os.path.join(temp_dir, filename)
        with open(file_path, 'w') as file:
            file.write(content)
    
    return temp_dir

def test_task_func():
    temp_dir = create_temp_directory_with_json_files()
    try:
        result = task_func(temp_dir)
        assert len(result) == 2
        assert all(os.path.join(temp_dir, f) in result for f in ['file1.json', 'file2.json'])
        
        # Verify contents of the files
        with open(os.path.join(temp_dir, 'file1.json'), 'r') as file:
            content = file.read()
            assert content == '{"key1": "value1"}'
        
        with open(os.path.join(temp_dir, 'file2.json'), 'r') as file:
            content = file.read()
            assert content == '{"key2": "value2 with \\"quotes\\""}'
    finally:
        shutil.rmtree(temp_dir)

def test_task_func_nonexistent_directory():
    with pytest.raises(FileNotFoundError) as exc_info:
        task_func('/nonexistent/directory')
    assert str(exc_info.value) == "Directory /nonexistent/directory not found."

def test_task_func_empty_directory():
    temp_dir = tempfile.mkdtemp()
    try:
        result = task_func(temp_dir)
        assert result == []
    finally:
        shutil.rmtree(temp_dir)