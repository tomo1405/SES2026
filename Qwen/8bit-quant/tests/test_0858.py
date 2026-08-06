import os
import shutil
import tempfile

import pytest
from src_0858 import task_func


@pytest.fixture
def setup_directories():
    source_dir = tempfile.mkdtemp()
    dest_dir = tempfile.mkdtemp()
    yield source_dir, dest_dir
    shutil.rmtree(source_dir)
    shutil.rmtree(dest_dir)

def test_task_func_no_files(setup_directories):
    source_dir, dest_dir = setup_directories
    extensions = ['.txt', '.pdf']
    result = task_func(source_dir, dest_dir, extensions)
    assert result == []

def test_task_func_with_files(setup_directories):
    source_dir, dest_dir = setup_directories
    extensions = ['.txt', '.pdf']
    files_to_create = ['file1.txt', 'file2.pdf', 'file3.docx']
    
    for file in files_to_create:
        with open(os.path.join(source_dir, file), 'w') as f:
            f.write('Test content')

    result = task_func(source_dir, dest_dir, extensions)
    expected_result = ['file1.txt', 'file2.pdf']
    assert sorted(result) == sorted(expected_result)

    for file in expected_result:
        assert os.path.exists(os.path.join(dest_dir, file))

    for file in files_to_create:
        if file not in expected_result:
            assert os.path.exists(os.path.join(source_dir, file))

def test_task_func_with_nonexistent_extension(setup_directories):
    source_dir, dest_dir = setup_directories
    extensions = ['.xyz']
    files_to_create = ['file1.txt', 'file2.pdf']
    
    for file in files_to_create:
        with open(os.path.join(source_dir, file), 'w') as f:
            f.write('Test content')

    result = task_func(source_dir, dest_dir, extensions)
    assert result == []

def test_task_func_permission_error(setup_directories, monkeypatch):
    source_dir, dest_dir = setup_directories
    extensions = ['.txt']

    def mock_shutil_move(src, dst):
        raise PermissionError("Permission denied")

    monkeypatch.setattr(shutil, 'move', mock_shutil_move)

    with open(os.path.join(source_dir, 'file1.txt'), 'w') as f:
        f.write('Test content')

    result = task_func(source_dir, dest_dir, extensions)
    assert result == []
    assert os.path.exists(os.path.join(source_dir, 'file1.txt'))