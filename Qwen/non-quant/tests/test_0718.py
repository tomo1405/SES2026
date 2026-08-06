import os
import sys
from configparser import ConfigParser

from src_0718 import task_func


def test_task_func_default_values():
    config, config_file = task_func()
    assert isinstance(config, ConfigParser)
    assert config_file == '/path/to/config.ini'
    assert PATH_TO_APPEND in sys.path
    assert os.path.exists(config_file)
    config.read(config_file)
    assert config.get('DEFAULT', 'path_to_append') == PATH_TO_APPEND

def test_task_func_custom_path():
    custom_path = '/custom/path'
    config, config_file = task_func(custom_path)
    assert isinstance(config, ConfigParser)
    assert config_file == '/path/to/config.ini'
    assert custom_path in sys.path
    assert os.path.exists(config_file)
    config.read(config_file)
    assert config.get('DEFAULT', 'path_to_append') == custom_path

def test_task_func_multiple_paths():
    custom_paths = ['/custom/path1', '/custom/path2']
    config, config_file = task_func(custom_paths)
    assert isinstance(config, ConfigParser)
    assert config_file == '/path/to/config.ini'
    for path in custom_paths:
        assert path in sys.path
    assert os.path.exists(config_file)
    config.read(config_file)
    assert config.get('DEFAULT', 'path_to_append') == ','.join(custom_paths)

def test_task_func_nonexistent_config_file():
    config_file = '/nonexistent/config.ini'
    config, returned_config_file = task_func(config_file=config_file)
    assert isinstance(config, ConfigParser)
    assert returned_config_file == config_file
    assert os.path.exists(config_file)
    config.read(config_file)
    assert config.get('DEFAULT', 'path_to_append') == PATH_TO_APPEND

def test_task_func_existing_config_file(tmpdir):
    config_file = str(tmpdir.join('config.ini'))
    with open(config_file, 'w') as f:
        f.write('[DEFAULT]\nexisting_key=existing_value\n')
    config, returned_config_file = task_func(config_file=config_file)
    assert isinstance(config, ConfigParser)
    assert returned_config_file == config_file
    assert os.path.exists(config_file)
    config.read(config_file)
    assert config.get('DEFAULT', 'existing_key') == 'existing_value'
    assert config.get('DEFAULT', 'path_to_append') == PATH_TO_APPEND