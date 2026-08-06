import pytest
from src_0392 import task_func

def test_task_func():
    directory = 'test_directory'
    archive_dir = 'test_archive'
    json_files = ['test_file1.json', 'test_file2.json']

    with pytest.raises(Exception):
        task_func(directory, archive_dir)

    assert os.path.exists(archive_dir)
    assert len(json_files) == 2
    assert len(error_messages) == 0