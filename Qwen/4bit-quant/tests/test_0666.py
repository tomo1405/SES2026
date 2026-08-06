import pytest
from src_0666 import task_func
import os
import shutil
import tempfile

@pytest.fixture
def setup_directories():
    src_dir = tempfile.mkdtemp()
    dst_dir = tempfile.mkdtemp()

    # Create some test files in the source directory
    with open(os.path.join(src_dir, 'test.txt'), 'w') as f:
        f.write('Test content')
    with open(os.path.join(src_dir, 'test.docx'), 'w') as f:
        f.write('Docx content')
    with open(os.path.join(src_dir, 'test.pdf'), 'w') as f:
        f.write('Pdf content')

    yield src_dir, dst_dir

    # Clean up temporary directories
    shutil.rmtree(src_dir)
    shutil.rmtree(dst_dir)

def test_task_func(setup_directories):
    src_dir, dst_dir = setup_directories

    # Call the function
    result = task_func(src_dir, dst_dir)

    # Check that the destination directory is returned
    assert result == dst_dir

    # Check that only the matching files were copied
    assert os.path.exists(os.path.join(dst_dir, 'test.txt'))
    assert os.path.exists(os.path.join(dst_dir, 'test.docx'))
    assert not os.path.exists(os.path.join(dst_dir, 'test.pdf'))

def test_task_func_no_matching_files(setup_directories):
    src_dir, dst_dir = setup_directories

    # Remove the matching files
    os.remove(os.path.join(src_dir, 'test.txt'))
    os.remove(os.path.join(src_dir, 'test.docx'))

    # Call the function
    result = task_func(src_dir, dst_dir)

    # Check that the destination directory is returned
    assert result == dst_dir

    # Check that no files were copied
    assert not os.listdir(dst_dir)