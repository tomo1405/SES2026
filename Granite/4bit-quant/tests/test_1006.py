import os
import tempfile
import urllib.error
import urllib.request
import zipfile

from src_1006 import task_func

def test_task_func():
    with tempfile.TemporaryDirectory() as temp_dir:
        save_path = os.path.join(temp_dir, "downloaded_file.zip")
        extract_path = os.path.join(temp_dir, "extracted_files")
        url = "https://example.com/my_file.zip"

        # Test successful download and extraction
        result = task_func(url, save_path, extract_path)
        assert result == extract_path
        assert os.path.exists(result)
        assert os.path.isfile(os.path.join(result, "my_file.txt"))

        # Test URL error handling
        url = "https://example.com/nonexistent_file.zip"
        result = task_func(url, save_path, extract_path)
        assert isinstance(result, str)
        assert result.startswith("URL Error:")