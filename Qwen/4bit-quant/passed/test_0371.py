import pytest
from src_0371 import task_func
import os
import json
import tempfile
import shutil

def create_temp_dir_with_json_files():
    temp_dir = tempfile.mkdtemp()
    json_files = [
        {"file_name": "data1.json", "content": {"key": "value1"}},
        {"file_name": "data2.json", "content": {"key": "value2"}}
    ]
    
    for file_info in json_files:
        file_path = os.path.join(temp_dir, file_info["file_name"])
        with open(file_path, 'w') as file:
            json.dump(file_info["content"], file)
    
    return temp_dir

def test_task_func():
    temp_dir = create_temp_dir_with_json_files()
    try:
        result = task_func(temp_dir)
        assert len(result) == 2
        assert all(os.path.exists(file) for file in result)
        
        for file in result:
            with open(file, 'r') as f:
                content = f.read()
                assert '\\\"' in content  # Check if escaping is done correctly
    finally:
        shutil.rmtree(temp_dir)

def test_task_func_non_existent_directory():
    with pytest.raises(FileNotFoundError, match="Directory .* not found."):
        task_func("/non/existent/directory")

def test_task_func_no_json_files():
    temp_dir = tempfile.mkdtemp()
    try:
        result = task_func(temp_dir)
        assert result == []
    finally:
        shutil.rmtree(temp_dir)