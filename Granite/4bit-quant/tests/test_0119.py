import os
import shutil


def task_func(directory, backup_directory):
    copied_files = []

    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)

    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            src = os.path.join(directory, filename)
            dst = os.path.join(backup_directory, filename)
            shutil.copy(src, dst)
            copied_files.append(dst)

    return copied_files

def test_task_func():
    directory = "/path/to/directory"
    backup_directory = "/path/to/backup_directory"
    expected_copied_files = ["/path/to/backup_directory/file1.json", "/path/to/backup_directory/file2.json"]

    # Mock the os.listdir() and os.makedirs() functions
    def mock_listdir(path):
        return ["file1.json", "file2.json"]

    def mock_makedirs(path):
        pass

    with mock_patch("os.listdir", side_effect=mock_listdir), mock_patch("os.makedirs", side_effect=mock_makedirs):
        copied_files = task_func(directory, backup_directory)
        assert copied_files == expected_copied_files