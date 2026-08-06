import pytest
from src_0666 import task_func

def test_task_func():
    src_dir = 'path/to/src/dir'
    dst_dir = 'path/to/dst/dir'
    FILE_PATTERNS = ['*.txt', '*.docx']

    # Test with no matching files
    matching_files = []
    with pytest.raises(ValueError):
        task_func(src_dir, dst_dir)

    # Test with matching files
    matching_files = ['file1.txt', 'file2.docx']
    with pytest.raises(ValueError):
        task_func(src_dir, dst_dir)

    # Test with invalid src_dir
    src_dir = 'invalid/path'
    with pytest.raises(ValueError):
        task_func(src_dir, dst_dir)

    # Test with invalid dst_dir
    dst_dir = 'invalid/path'
    with pytest.raises(ValueError):
        task_func(src_dir, dst_dir)

    # Test with valid src_dir and dst_dir
    src_dir = 'path/to/src/dir'
    dst_dir = 'path/to/dst/dir'
    task_func(src_dir, dst_dir)
    assert os.path.exists(dst_dir)
    assert os.path.isdir(dst_dir)
    assert os.path.exists(os.path.join(dst_dir, 'file1.txt'))
    assert os.path.exists(os.path.join(dst_dir, 'file2.docx'))