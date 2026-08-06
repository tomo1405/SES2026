import pytest
from src_0351 import task_func
import os
import shutil
from glob import glob
import tempfile

@pytest.fixture
def setup_folders():
    src_folder = tempfile.mkdtemp()
    dst_folder = tempfile.mkdtemp()
    yield src_folder, dst_folder
    shutil.rmtree(src_folder)
    shutil.rmtree(dst_folder)

@pytest.fixture
def create_files_in_src(src_folder):
    files = ['file1.txt', 'file2.txt', 'file3.txt']
    for file in files:
        with open(os.path.join(src_folder, file), 'w') as f:
            f.write('test content')
    return files

def test_task_func_success(setup_folders, create_files_in_src):
    src_folder, dst_folder = setup_folders
    result = task_func(src_folder, dst_folder)
    assert result['success'] == True
    assert result['message'] == 'All files compressed and moved successfully.'
    assert result['failed_files'] == []
    assert len(glob(os.path.join(dst_folder, '*.gz'))) == 3

def test_task_func_failure(setup_folders, create_files_in_src, monkeypatch):
    src_folder, dst_folder = setup_folders
    
    def mock_subprocess_popen(args):
        class MockProcess:
            def wait(self):
                return 1
        return MockProcess()
    
    monkeypatch.setattr(subprocess, 'Popen', mock_subprocess_popen)
    
    result = task_func(src_folder, dst_folder)
    assert result['success'] == False
    assert result['message'] == 'Some files failed to compress or move.'
    assert len(result['failed_files']) == 3
    assert len(glob(os.path.join(src_folder, '*.gz'))) == 0

def test_task_func_nonexistent_src(setup_folders):
    _, dst_folder = setup_folders
    with pytest.raises(ValueError) as excinfo:
        task_func('nonexistent_src', dst_folder)
    assert str(excinfo.value) == "Source folder 'nonexistent_src' does not exist."

def test_task_func_nonexistent_dst(setup_folders, create_files_in_src):
    src_folder, _ = setup_folders
    with pytest.raises(ValueError) as excinfo:
        task_func(src_folder, 'nonexistent_dst')
    assert str(excinfo.value) == "Destination folder 'nonexistent_dst' does not exist."