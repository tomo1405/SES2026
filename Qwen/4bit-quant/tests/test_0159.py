import gzip
import json
import os
import urllib

import pytest
from src_0159 import task_func


def test_task_func(tmpdir):
    # Arrange
    url_str = "https://jsonplaceholder.typicode.com/posts/1"
    file_path = str(tmpdir / "test_output.json.gz")
    
    # Act
    result = task_func(url_str, file_path)
    
    # Assert
    assert result == file_path
    assert os.path.exists(file_path)
    
    with gzip.open(file_path, 'rb') as f_in:
        decompressed_data = f_in.read()
        json_data = json.loads(decompressed_data.decode())
    
    assert isinstance(json_data, dict)
    assert 'userId' in json_data
    assert 'id' in json_data
    assert 'title' in json_data
    assert 'body' in json_data

def test_task_func_invalid_url(tmpdir):
    # Arrange
    url_str = "https://invalid-url.com"
    file_path = str(tmpdir / "test_output.json.gz")
    
    # Act & Assert
    with pytest.raises(urllib.error.URLError):
        task_func(url_str, file_path)

def test_task_func_non_json_response(tmpdir):
    # Arrange
    url_str = "https://httpbin.org/status/404"
    file_path = str(tmpdir / "test_output.json.gz")
    
    # Act & Assert
    with pytest.raises(json.JSONDecodeError):
        task_func(url_str, file_path)