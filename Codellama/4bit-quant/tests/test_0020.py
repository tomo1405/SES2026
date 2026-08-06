import pytest
from src_0020 import task_func

def test_task_func_valid_directory():
    directory = 'path/to/directory'
    zip_file_path = task_func(directory)
    assert zip_file_path == os.path.join(directory, 'files.zip')
    with zipfile.ZipFile(zip_file_path, 'r') as zipf:
        assert zipf.namelist() == [os.path.basename(file) for file in files]

def test_task_func_invalid_directory():
    directory = 'path/to/invalid/directory'
    with pytest.raises(FileNotFoundError):
        task_func(directory)

def test_task_func_empty_directory():
    directory = 'path/to/empty/directory'
    zip_file_path = task_func(directory)
    assert zip_file_path is None