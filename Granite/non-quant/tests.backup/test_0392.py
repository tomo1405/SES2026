import os
import glob
import shutil
from unittest import mock

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
    with mock.patch('os.path.exists') as mock_exists, \
         mock.patch('os.makedirs') as mock_makedirs, \
         mock.patch('glob.glob') as mock_glob, \
         mock.patch('shutil.move') as mock_move:

        mock_exists.return_value = False
        mock_glob.return_value = ['file1.json', 'file2.json']
        mock_move.side_effect = [Exception('Test exception 1'), None]

        result = task_func('/path/to/directory')

        mock_exists.assert_called_with('archive')
        mock_makedirs.assert_called_with('archive')
        mock_glob.assert_called_with('/path/to/directory/*.json')
        mock_move.assert_has_calls([
            mock.call('file1.json', 'archive'),
            mock.call('file2.json', 'archive')
        ])
        assert result == (False, ['Unable to move file1.json due to Test exception 1'])