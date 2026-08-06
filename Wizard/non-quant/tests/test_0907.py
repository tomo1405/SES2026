python
import pytest
from src_0907 import task_func

def test_task_func():
    source_dir = 'source_dir'
    target_dir = 'target_dir'
    archive_name = 'archive.zip'
    archive_path = task_func(source_dir, target_dir, archive_name)
    assert os.path.exists(archive_path)
    assert os.path.isfile(archive_path)
    assert os.path.exists(os.path.join(target_dir, 'file_processed.txt'))
    assert not os.path.exists(os.path.join(source_dir, 'file_processed.txt'))