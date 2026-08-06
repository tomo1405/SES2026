import pytest
from src_0666 import task_func

def test_task_func():
    src_dir = 'tests/test_data/src'
    dst_dir = 'tests/test_data/dst'
    FILE_PATTERNS = ['*.txt', '*.docx']

    # Test with no files in src_dir
    assert task_func(src_dir, dst_dir) == dst_dir

    # Test with files in src_dir
    matching_files = list(itertools.chain.from_iterable(
        fnmatch.filter(os.listdir(src_dir), pattern) for pattern in FILE_PATTERNS))
    for filename in matching_files:
        shutil.copy2(os.path.join(src_dir, filename), dst_dir)
    assert task_func(src_dir, dst_dir) == dst_dir

    # Test with invalid src_dir
    with pytest.raises(ValueError):
        task_func('invalid_dir', dst_dir)

    # Test with invalid dst_dir
    with pytest.raises(ValueError):
        task_func(src_dir, 'invalid_dir')