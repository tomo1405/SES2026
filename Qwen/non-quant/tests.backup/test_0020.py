import pytest
from src_0020 import task_func
import os
import zipfile

def test_task_func_directory_not_found():
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func('/nonexistent_directory')
    assert str(excinfo.value) == "Directory '/nonexistent_directory' not found."

def test_task_func_no_files_in_directory(tmpdir):
    result = task_func(str(tmpdir))
    assert result is None

def test_task_func_with_files(tmpdir):
    file1 = tmpdir.join('file1.txt')
    file1.write('content of file1')
    file2 = tmpdir.join('file2.txt')
    file2.write('content of file2')

    zip_file_path = task_func(str(tmpdir))
    assert os.path.exists(zip_file_path)

    with zipfile.ZipFile(zip_file_path, 'r') as zipf:
        assert set(zipf.namelist()) == {'file1.txt', 'file2.txt'}

def test_task_func_with_subdirectories(tmpdir):
    subdir = tmpdir.mkdir('subdir')
    file1 = subdir.join('file1.txt')
    file1.write('content of file1')

    result = task_func(str(tmpdir))
    assert result is None

def test_task_func_with_existing_zip_file(tmpdir):
    zip_file_path = tmpdir.join('files.zip')
    zip_file_path.write('existing content')

    file1 = tmpdir.join('file1.txt')
    file1.write('content of file1')

    new_zip_file_path = task_func(str(tmpdir))
    assert new_zip_file_path != str(zip_file_path)
    assert os.path.exists(new_zip_file_path)

    with zipfile.ZipFile(new_zip_file_path, 'r') as zipf:
        assert set(zipf.namelist()) == {'file1.txt'}