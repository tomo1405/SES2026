import pytest
from src_0327 import task_func
import os
import tempfile
import shutil

@pytest.fixture
def create_temp_dir():
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    shutil.rmtree(temp_dir)

@pytest.fixture
def create_bat_files(temp_dir):
    bat_file1 = os.path.join(temp_dir, 'test1.bat')
    bat_file2 = os.path.join(temp_dir, 'test2.bat')
    with open(bat_file1, 'w') as f:
        f.write('@echo off\necho Hello World 1\nexit /b 0')
    with open(bat_file2, 'w') as f:
        f.write('@echo off\necho Hello World 2\nexit /b 1')
    return [bat_file1, bat_file2]

def test_task_func(create_temp_dir, create_bat_files):
    results = task_func(create_temp_dir)
    assert len(results) == 2
    assert ('test1.bat', 0) in results
    assert ('test2.bat', 1) in results

def test_task_func_no_bat_files(create_temp_dir):
    results = task_func(create_temp_dir)
    assert results == []

def test_task_func_with_non_executable(create_temp_dir):
    non_executable_file = os.path.join(create_temp_dir, 'non_executable.bat')
    with open(non_executable_file, 'w') as f:
        f.write('@echo off\necho This file is not executable\nexit /b 1')
    os.chmod(non_executable_file, 0o444)  # Make the file read-only

    results = task_func(create_temp_dir)
    assert len(results) == 1
    assert ('non_executable.bat', None) in results

def test_task_func_with_error(create_temp_dir):
    error_file = os.path.join(create_temp_dir, 'error.bat')
    with open(error_file, 'w') as f:
        f.write('@echo off\necho This file will cause an error\nexit /b 1')

    def mock_subprocess_popen(*args, **kwargs):
        raise Exception("Mocked subprocess error")

    with pytest.raises(Exception) as excinfo:
        with patch('src_0327.subprocess.Popen', side_effect=mock_subprocess_popen):
            task_func(create_temp_dir)

    assert str(excinfo.value) == "Mocked subprocess error"