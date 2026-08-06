import pytest
from src_0392 import task_func

def test_task_func_with_valid_input():
    directory = 'test_directory'
    archive_dir = 'test_archive_dir'
    expected_result = (True, [])

    result = task_func(directory, archive_dir)

    assert result == expected_result

def test_task_func_with_invalid_input():
    directory = 'test_directory'
    archive_dir = 'test_archive_dir'
    expected_result = (False, ['Unable to move test_file.json due to [Error message]'])

    with pytest.raises(Exception) as e:
        result = task_func(directory, archive_dir)

    assert result == expected_result
    assert str(e) == 'Unable to move test_file.json due to [Error message]'