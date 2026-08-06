import subprocess
import os
import shutil
from glob import glob
from src_0351 import task_func
def test_task_func():
    src_folder = 'source_folder'
    dst_folder = 'destination_folder'
    # Mock the os.path.isdir function to return True for both source and destination folders
    with mock.patch('os.path.isdir') as mock_isdir:
        mock_isdir.return_value = True
        result = task_func(src_folder, dst_folder)
        assert result['success'] == True
        assert result['message'] == 'All files compressed and moved successfully.'
        assert result['failed_files'] == []
def test_task_func_source_folder_does_not_exist():
    src_folder = 'source_folder'
    dst_folder = 'destination_folder'
    # Mock the os.path.isdir function to return False for the source folder
    with mock.patch('os.path.isdir') as mock_isdir:
        mock_isdir.side_effect = [False, True]
        with pytest.raises(ValueError) as excinfo:
            task_func(src_folder, dst_folder)
        assert str(excinfo.value) == f"Source folder '{src_folder}' does not exist."
def test_task_func_destination_folder_does_not_exist():
    src_folder = 'source_folder'
    dst_folder = 'destination_folder'
    # Mock the os.path.isdir function to return False for the destination folder
    with mock.patch('os.path.isdir') as mock_isdir:
        mock_isdir.side_effect = [True, False]
        with pytest.raises(ValueError) as excinfo:
            task_func(src_folder, dst_folder)
        assert str(excinfo.value) == f"Destination folder '{dst_folder}' does not exist."
def test_task_func_compress_and_move_files():
    src_folder = 'source_folder'
    dst_folder = 'destination_folder'
    # Mock the subprocess.Popen and shutil.move functions to simulate successful compression and moving of files
    with mock.patch('subprocess.Popen') as mock_popen, mock.patch('shutil.move') as mock_move:
        mock_popen.return_value.wait.return_value = 0
        task_func(src_folder, dst_folder)
        mock_popen.assert_has_calls([mock.call(['gzip', file]) for file in glob(os.path.join(src_folder, '*'))])
        mock_move.assert_has_calls([mock.call(file, dst_folder) for file in glob(os.path.join(src_folder, '*.gz'))])
def test_task_func_compress_and_move_files_with_failures():
    src_folder = 'source_folder'
    dst_folder = 'destination_folder'
    failed_files = ['file1.txt', 'file2.txt']
    # Mock the subprocess.Popen and shutil.move functions to simulate failed compression and moving of files
    with mock.patch('subprocess.Popen') as mock_popen, mock.patch('shutil.move') as mock_move:
        mock_popen.return_value.wait.side_effect = [0, 1] # First file succeeds, second file fails
        mock_move.side_effect = [Exception('Failed to move file.')] # Simulate failure to move file
        result = task_func(src_folder, dst_folder)
        assert result['success'] == False
        assert result['message'] == 'Some files failed to compress or move.'
        assert result['failed_files'] == failed_files