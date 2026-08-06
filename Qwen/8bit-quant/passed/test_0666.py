import pytest
from src_0666 import task_func
import shutil
import os
import tempfile

@pytest.fixture
def setup_directories():
    src_dir = tempfile.mkdtemp()
    dst_dir = tempfile.mkdtemp()

    # Create some test files in the source directory
    with open(os.path.join(src_dir, 'test1.txt'), 'w') as f:
        f.write('Test content 1')
    with open(os.path.join(src_dir, 'test2.docx'), 'w') as f:
        f.write('Test content 2')
    with open(os.path.join(src_dir, 'test3.pdf'), 'w') as f:
        f.write('Test content 3')

    yield src_dir, dst_dir

    # Clean up temporary directories
    shutil.rmtree(src_dir)
    shutil.rmtree(dst_dir)

def test_task_func(setup_directories):
    src_dir, dst_dir = setup_directories

    # Run the function
    result = task_func(src_dir, dst_dir)

    # Check if the destination directory is returned
    assert result == dst_dir

    # Check if only the matching files are copied
    assert os.path.exists(os.path.join(dst_dir, 'test1.txt'))
    assert os.path.exists(os.path.join(dst_dir, 'test2.docx'))
    assert not os.path.exists(os.path.join(dst_dir, 'test3.pdf'))

def test_task_func_no_matching_files(setup_directories):
    src_dir, dst_dir = setup_directories

    # Remove all files that match the patterns
    for filename in os.listdir(src_dir):
        if filename.endswith('.txt') or filename.endswith('.docx'):
            os.remove(os.path.join(src_dir, filename))

    # Run the function
    result = task_func(src_dir, dst_dir)

    # Check if the destination directory is returned
    assert result == dst_dir

    # Check if no files are copied
    assert len(os.listdir(dst_dir)) == 0