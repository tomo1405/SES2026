import configparser
import os
import shutil
from src_0015 import task_func

def test_task_func():
    config_file_path = 'path/to/config/file'
    archive_dir = '/home/user/archive'
    project_dir = 'path/to/project/directory'
    config = configparser.ConfigParser()
    config.read(config_file_path)
    config.set('Project', 'directory', project_dir)

    # Mock the os.path.isdir and os.path.isfile functions
    def mock_os_path_isdir(path):
        if path == project_dir:
            return True
        else:
            return False

    def mock_os_path_isfile(path):
        if path == archive_dir:
            return False
        else:
            return True

    with patch('os.path.isdir', side_effect=mock_os_path_isdir):
        with patch('os.path.isfile', side_effect=mock_os_path_isfile):
            result = task_func(config_file_path, archive_dir)
            assert result == True