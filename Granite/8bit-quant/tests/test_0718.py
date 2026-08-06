from src_0718 import task_func


def test_task_func():
    # Test case 1: path_to_append is a list
    path_to_append = ['/path1', '/path2', '/path3']
    config, config_file = task_func(path_to_append=path_to_append)
    assert config.get('DEFAULT', 'path_to_append') == ','.join(path_to_append)
    assert config_file == '/path/to/config.ini'

    # Test case 2: path_to_append is a string
    path_to_append = '/path/to/whatever'
    config, config_file = task_func(path_to_append=path_to_append)
    assert config.get('DEFAULT', 'path_to_append') == path_to_append
    assert config_file == '/path/to/config.ini'

    # Test case 3: config_file does not exist
    path_to_append = '/path/to/whatever'
    config, config_file = task_func(path_to_append=path_to_append, config_file='/tmp/config.ini')
    assert config.get('DEFAULT', 'path_to_append') == path_to_append
    assert config_file == '/tmp/config.ini'