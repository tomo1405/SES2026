import pytest
from src_0858 import task_func
import os
import tempfile

@pytest.fixture
def setup_directories():
    source_dir = tempfile.mkdtemp()
    dest_dir = tempfile.mkdtemp()
    yield source_dir, dest_dir
    shutil.rmtree(source_dir)
    shutil.rmtree(dest_dir)

def test_task_func_no_files(setup_directories):
    source_dir, dest_dir = setup_directories
    extensions = ['.txt', '.py']
    result = task_func(source_dir, dest_dir, extensions)
    assert result == []

def test_task_func_with_files(setup_directories):
    source_dir, dest_dir = setup_directories
    extensions = ['.txt', '.py']
    files_to_create = ['file1.txt', 'file2.py', 'file3.docx']
    
    for file_name in files_to_create:
        with open(os.path.join(source_dir, file_name), 'w') as f:
            f.write('Test content')

    result = task_func(source_dir, dest_dir, extensions)
    assert sorted(result) == ['file1.txt', 'file2.py']
    assert not os.path.exists(os.path.join(source_dir, 'file1.txt'))
    assert not os.path.exists(os.path.join(source_dir, 'file2.py'))
    assert os.path.exists(os.path.join(dest_dir, 'file1.txt'))
    assert os.path.exists(os.path.join(dest_dir, 'file2.py'))

def test_task_func_with_nonexistent_source_dir(setup_directories):
    _, dest_dir = setup_directories
    extensions = ['.txt', '.py']
    with pytest.raises(FileNotFoundError):
        task_func('nonexistent_source', dest_dir, extensions)

def test_task_func_with_nonexistent_dest_dir(setup_directories):
    source_dir, _ = setup_directories
    extensions = ['.txt', '.py']
    with pytest.raises(FileNotFoundError):
        task_func(source_dir, 'nonexistent_dest', extensions)

def test_task_func_with_empty_extensions(setup_directories):
    source_dir, dest_dir = setup_directories
    extensions = []
    result = task_func(source_dir, dest_dir, extensions)
    assert result == []

def test_task_func_with_invalid_extension(setup_directories):
    source_dir, dest_dir = setup_directories
    extensions = ['.xyz']
    files_to_create = ['file1.xyz']
    
    for file_name in files_to_create:
        with open(os.path.join(source_dir, file_name), 'w') as f:
            f.write('Test content')

    result = task_func(source_dir, dest_dir, extensions)
    assert result == []