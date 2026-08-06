import configparser
import os
import shutil
from src_0015 import task_func

def test_task_func():
    config_file_path = 'path/to/config/file'
    archive_dir = '/home/user/archive'
    project_dir = 'path/to/project/directory'
    archive_file = f'{archive_dir}/{os.path.basename(project_dir)}.zip'

    # Mock the configparser and os modules
    config_mock = configparser.ConfigParser()
    config_mock.read.return_value = True
    config_mock.get.return_value = project_dir
    os_mock = mock.Mock()
    os_mock.path.isdir.return_value = True
    os_mock.path.basename.return_value = 'project_dir'
    os_mock.path.splitext.return_value = ('/path/to/archive/project_dir', '.zip')
    os_mock.path.isfile.return_value = False

    # Monkey patch the modules
    with mock.patch('configparser.ConfigParser', return_value=config_mock), \
         mock.patch('os', os_mock):

        # Call the function and assert the result
        result = task_func(config_file_path, archive_dir)
        assert result is True

        # Assert that the expected methods were called
        config_mock.read.assert_called_once_with(config_file_path)
        config_mock.get.assert_called_once_with('Project', 'directory')
        os_mock.path.isdir.assert_called_once_with(project_dir)
        os_mock.path.basename.assert_called_once_with(project_dir)
        os_mock.path.splitext.assert_called_once_with(archive_file)
        shutil.make_archive.assert_called_once_with(base_name='/path/to/archive/project_dir', format='zip', root_dir=project_dir)
        os_mock.path.isfile.assert_called_once_with(archive_file)