python
import sys
import os
import pytest
from configparser import ConfigParser

# Constants
PATH_TO_APPEND = '/path/to/whatever'
CONFIG_FILE = '/path/to/config.ini'

def task_func(path_to_append=PATH_TO_APPEND, config_file=CONFIG_FILE):
    if isinstance(path_to_append, list):
        for path in path_to_append:
            sys.path.append(path)
    else:
        sys.path.append(path_to_append)

    config = ConfigParser()

    # Create the file if it doesn't exist
    if not os.path.exists(config_file):
        open(config_file, 'a').close()

    config.read(config_file)
    path_str = ','.join(path_to_append) if isinstance(path_to_append, list) else path_to_append
    config.set('DEFAULT', 'path_to_append', path_str)

    with open(config_file, 'w') as file:
        config.write(file)

    return config, config_file

def test_task_func():
    # Test case 1: path_to_append is a string
    config, config_file = task_func(path_to_append='/path/to/new/whatever')
    assert config.get('DEFAULT', 'path_to_append') == '/path/to/new/whatever'
    assert config_file == '/path/to/config.ini'

    # Test case 2: path_to_append is a list
    config, config_file = task_func(path_to_append=['/path/to/new/whatever', '/path/to/another/whatever'])
    assert config.get('DEFAULT', 'path_to_append') == '/path/to/new/whatever,/path/to/another/whatever'
    assert config_file == '/path/to/config.ini'

    # Test case 3: config_file is a different path
    config, config_file = task_func(config_file='/path/to/new/config.ini')
    assert config.get('DEFAULT', 'path_to_append') == '/path/to/whatever'
    assert config_file == '/path/to/new/config.ini'

    # Test case 4: config_file doesn't exist
    with pytest.raises(FileNotFoundError):
        task_func(config_file='/path/to/nonexistent/config.ini')