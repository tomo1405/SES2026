import os
import glob
import shutil
import time
import pytest

# Constants
FILE_EXTENSIONS = ['.txt', '.csv', '.xlsx', '.docx', '.pdf']

def task_func(my_path: str, days_old: int) -> str:

    archive_dir = os.path.join(my_path, 'archive')
    os.makedirs(archive_dir, exist_ok=True)

    for ext in FILE_EXTENSIONS:
        files = glob.glob(os.path.join(my_path, '*' + ext))
        for file in files:
            if os.path.isfile(file) and os.path.getmtime(file) < time.time() - days_old * 86400:
                shutil.move(file, archive_dir)

    return archive_dir

def test_task_func():
    test_path = "/path/to/test/files"
    test_days_old = 7
    expected_archive_dir = os.path.join(test_path, 'archive')

    archive_dir = task_func(test_path, test_days_old)

    assert archive_dir == expected_archive_dir
    assert os.path.exists(archive_dir)
    assert len(os.listdir(archive_dir)) > 0

if __name__ == "__main__":
    pytest.main()