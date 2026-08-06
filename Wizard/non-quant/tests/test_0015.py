python
import configparser
import os
import shutil
import pytest

def task_func(config_file_path, archieve_dir ='/home/user/archive'):
    config = configparser.ConfigParser()
    config.read(config_file_path)

    project_dir = config.get('Project', 'directory')

    if not os.path.isdir(project_dir):
        raise FileNotFoundError(f'Directory {project_dir} does not exist.')

    archive_file = f'{archieve_dir}/{os.path.basename(project_dir)}.zip'
    
    # Using shutil to create the zip archive
    shutil.make_archive(base_name=os.path.splitext(archive_file)[0], format='zip', root_dir=project_dir)

    if not os.path.isfile(archive_file):
        raise Exception(f"Failed to create archive {archive_file}")

    return True

def test_task_func():
    # Test case 1: Valid config file path and archive directory
    config_file_path = 'config.ini'
    archieve_dir = '/home/user/archive'
    assert task_func(config_file_path, archieve_dir) == True

    # Test case 2: Invalid config file path
    config_file_path = 'invalid_config.ini'
    with pytest.raises(FileNotFoundError):
        task_func(config_file_path)

    # Test case 3: Invalid archive directory
    config_file_path = 'config.ini'
    archieve_dir = '/invalid/archive/directory'
    with pytest.raises(Exception):
        task_func(config_file_path, archieve_dir)