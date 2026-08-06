import pytest
from src_0015 import task_func

def test_task_func_valid_config():
    config_file_path = 'path/to/config/file'
    archieve_dir = '/home/user/archive'
    project_dir = 'path/to/project/directory'

    config = configparser.ConfigParser()
    config.read(config_file_path)
    config.set('Project', 'directory', project_dir)

    with pytest.raises(FileNotFoundError):
        task_func(config_file_path, archieve_dir)

    assert os.path.isfile(f'{archieve_dir}/{os.path.basename(project_dir)}.zip')

def test_task_func_invalid_config():
    config_file_path = 'path/to/config/file'
    archieve_dir = '/home/user/archive'
    project_dir = 'path/to/project/directory'

    config = configparser.ConfigParser()
    config.read(config_file_path)
    config.set('Project', 'directory', project_dir)

    with pytest.raises(Exception):
        task_func(config_file_path, archieve_dir)

    assert not os.path.isfile(f'{archieve_dir}/{os.path.basename(project_dir)}.zip')