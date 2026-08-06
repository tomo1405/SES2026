import pytest
from src_0020 import task_func
import os
import glob
import zipfile

def test_task_func_valid_directory():
    # Create a temporary directory and populate it with some files
    import tempfile
    import shutil
    temp_dir = tempfile.mkdtemp()
    try:
        # Create some files in the temporary directory
        file_content = b"file content"
        file_paths = []
        for i in range(3):
            file_path = os.path.join(temp_dir, f"file_{i}.txt")
            with open(file_path, 'w') as f:
                f.write(file_content)
            file_paths.append(file_path)

        # Call the function
        result = task_func(temp_dir)

        # Check if the zip file was created and contains the files
        assert os.path.exists(result)
        with zipfile.ZipFile(result, 'r') as zipf:
            assert len(zipf.namelist()) == len(file_paths)
            for file_path in file_paths:
                assert zipf.getinfo(os.path.basename(file_path))
    finally:
            shutil.rmtree(temp_dir)

def test_task_func_invalid_directory():
    with pytest.raises(FileNotFoundError):
        task_func("nonexistent_directory")