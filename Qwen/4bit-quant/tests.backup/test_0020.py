import pytest
from src_0020 import task_func
import os
import zipfile

def test_task_func_directory_not_found():
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func('/non_existent_directory')
    assert str(excinfo.value) == "Directory '/non_existent_directory' not found."

def test_task_func_no_files():
    temp_dir = 'temp_empty_dir'
    os.makedirs(temp_dir)
    result = task_func(temp_dir)
    assert result is None
    os.rmdir(temp_dir)

def test_task_func_with_files(tmpdir):
    # Create temporary directory and add some files
    temp_dir = tmpdir.mkdir('temp_dir')
    temp_dir.join('file1.txt').write('content1')
    temp_dir.join('file2.txt').write('content2')

    result = task_func(str(temp_dir))
    assert result == os.path.join(str(temp_dir), 'files.zip')

    # Check if the zip file contains the correct files
    with zipfile.ZipFile(result, 'r') as zipf:
        assert set(zipf.namelist()) == {'file1.txt', 'file2.txt'}

# Clean up after tests
def teardown_module(module):
    if os.path.exists('temp_empty_dir'):
        os.rmdir('temp_empty_dir')