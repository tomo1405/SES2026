import pytest
from src_0666 import task_func


def test_task_func():
    src_dir = 'tests/test_data/src'
    dst_dir = 'tests/test_data/dst'
    expected_files = ['file1.txt', 'file2.docx']

    task_func(src_dir, dst_dir)

    assert os.path.isdir(dst_dir)
    assert len(os.listdir(dst_dir)) == len(expected_files)
    for filename in expected_files:
        assert os.path.isfile(os.path.join(dst_dir, filename))