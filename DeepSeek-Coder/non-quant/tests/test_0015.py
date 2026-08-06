import pytest
from src_0015 import task_func

@pytest.fixture
def config_file_path():
    return 'path/to/config.ini'

@pytest.fixture
def archive_dir():
    return '/home/user/archive'

def test_task_func(config_file_path, archive_dir):
    assert task_func(config_file_path, archive_dir) == True