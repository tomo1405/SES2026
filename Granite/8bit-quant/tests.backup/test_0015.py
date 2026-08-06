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
    config_file_path = 'config.ini'
    archive_dir = '/home/user/archive'
    project_dir = '/home/user/project'
    archive_file = f'{archive_dir}/{os.path.basename(project_dir)}.zip'

    # Mock the configparser and os modules
    config = configparser.ConfigParser()
    config.read.return_value = True
    config.get.return_value = project_dir
    os.path.isdir.return_value = True
    os.path.basename.return_value = 'project'

    # Mock the shutil module
    shutil.make_archive.return_value = archive_file

    # Call the function and assert the expected output
    result = task_func(config_file_path, archive_dir)
    assert result == True
    assert os.path.isfile(archive_file)

    # Clean up the archive file
    os.remove(archive_file)

if __name__ == '__main__':
    pytest.main()