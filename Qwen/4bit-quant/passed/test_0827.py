import pytest
from src_0827 import task_func
import os
import shutil
import tempfile

@pytest.fixture
def setup_directories():
    # Create temporary directories for source and target
    source_dir = tempfile.mkdtemp()
    target_dir = tempfile.mkdtemp()
    yield source_dir, target_dir
    # Clean up directories after tests
    shutil.rmtree(source_dir)
    shutil.rmtree(target_dir)

def test_task_func_no_files(setup_directories):
    source_dir, target_dir = setup_directories
    assert task_func(source_dir, target_dir) == 0

def test_task_func_with_txt_file(setup_directories):
    source_dir, target_dir = setup_directories
    with open(os.path.join(source_dir, 'test.txt'), 'w') as f:
        f.write('Sample text')
    assert task_func(source_dir, target_dir) == 1
    assert os.path.exists(os.path.join(target_dir, 'test.txt'))

def test_task_func_with_doc_file(setup_directories):
    source_dir, target_dir = setup_directories
    with open(os.path.join(source_dir, 'test.doc'), 'w') as f:
        f.write('Sample doc')
    assert task_func(source_dir, target_dir) == 1
    assert os.path.exists(os.path.join(target_dir, 'test.doc'))

def test_task_func_with_docx_file(setup_directories):
    source_dir, target_dir = setup_directories
    with open(os.path.join(source_dir, 'test.docx'), 'w') as f:
        f.write('Sample docx')
    assert task_func(source_dir, target_dir) == 1
    assert os.path.exists(os.path.join(target_dir, 'test.docx'))

def test_task_func_with_non_matching_file(setup_directories):
    source_dir, target_dir = setup_directories
    with open(os.path.join(source_dir, 'test.pdf'), 'w') as f:
        f.write('Sample pdf')
    assert task_func(source_dir, target_dir) == 0
    assert not os.path.exists(os.path.join(target_dir, 'test.pdf'))

def test_task_func_source_directory_not_exists():
    with pytest.raises(FileNotFoundError):
        task_func('/nonexistent', '/target')

def test_task_func_target_directory_created(setup_directories):
    source_dir, target_dir = setup_directories
    with open(os.path.join(source_dir, 'test.txt'), 'w') as f:
        f.write('Sample text')
    task_func(source_dir, target_dir)
    assert os.path.exists(target_dir)