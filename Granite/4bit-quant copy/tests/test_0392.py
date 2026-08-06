import os
import glob
import shutil
import pytest

def task_func(directory, archive_dir='archive'):
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    json_files = glob.glob(os.path.join(directory, '*.json'))
    error_messages = []

    for json_file in json_files:
        try:
            shutil.move(json_file, archive_dir)
        except Exception as e:
            error_message = f'Unable to move {json_file} due to {str(e)}'
            error_messages.append(error_message)

    return (len(error_messages) == 0, error_messages)

def test_task_func():
    directory = 'test_directory'
    archive_dir = 'test_archive'
    os.makedirs(directory, exist_ok=True)
    json_file = os.path.join(directory, 'test_file.json')
    with open(json_file, 'w') as f:
        f.write('test content')
    expected_error_messages = []
    expected_result = (True, expected_error_messages)
    result = task_func(directory, archive_dir)
    assert result == expected_result
    os.remove(json_file)
    os.rmdir(directory)
    os.rmdir(archive_dir)

if __name__ == '__main__':
    pytest.main()