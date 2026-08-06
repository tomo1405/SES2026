import pytest
from src_0351 import task_func
import os
import shutil
import tempfile

@pytest.fixture
def setup_folders():
    src_folder = tempfile.mkdtemp(prefix='src_')
    dst_folder = tempfile.mkdtemp(prefix='dst_')
    yield src_folder, dst_folder
    shutil.rmtree(src_folder)
    shutil.rmtree(dst_folder)

def test_task_func_success(setup_folders):
    src_folder, dst_folder = setup_folders
    # Create some test files in the source folder
    with open(os.path.join(src_folder, 'file1.txt'), 'w') as f:
        f.write('Test content 1')
    with open(os.path.join(src_folder, 'file2.txt'), 'w') as f:
        f.write('Test content 2')

    result = task_func(src_folder, dst_folder)

    assert result['success'] == True
    assert result['message'] == 'All files compressed and moved successfully.'
    assert result['failed_files'] == []

    # Check that the compressed files are in the destination folder
    assert os.path.exists(os.path.join(dst_folder, 'file1.txt.gz'))
    assert os.path.exists(os.path.join(dst_folder, 'file2.txt.gz'))

def test_task_func_failure(setup_folders):
    src_folder, dst_folder = setup_folders
    # Create a test file in the source folder
    with open(os.path.join(src_folder, 'file1.txt'), 'w') as f:
        f.write('Test content 1')

    # Simulate a failure by making the destination folder read-only
    os.chmod(dst_folder, 0o444)

    result = task_func(src_folder, dst_folder)

    assert result['success'] == False
    assert result['message'] == 'Some files failed to compress or move.'
    assert result['failed_files'] == ['file1.txt.gz']

    # Check that the compressed file is still in the source folder
    assert os.path.exists(os.path.join(src_folder, 'file1.txt.gz'))

def test_task_func_nonexistent_src(setup_folders):
    _, dst_folder = setup_folders
    src_folder = '/nonexistent_src_folder'

    with pytest.raises(ValueError) as excinfo:
        task_func(src_folder, dst_folder)

    assert str(excinfo.value) == f"Source folder '{src_folder}' does not exist."

def test_task_func_nonexistent_dst(setup_folders):
    src_folder, _ = setup_folders
    dst_folder = '/nonexistent_dst_folder'

    with pytest.raises(ValueError) as excinfo:
        task_func(src_folder, dst_folder)

    assert str(excinfo.value) == f"Destination folder '{dst_folder}' does not exist."