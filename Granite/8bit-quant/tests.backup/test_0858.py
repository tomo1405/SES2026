import pytest
from src_0858 import task_func

def test_task_func():
    SOURCE_DIR = 'source_directory'
    DEST_DIR = 'destination_directory'
    EXTENSIONS = ['.txt', '.csv']

    transferred_files = task_func(SOURCE_DIR, DEST_DIR, EXTENSIONS)

    assert isinstance(transferred_files, list)
    for file in transferred_files:
        assert os.path.isfile(os.path.join(DEST_DIR, file))