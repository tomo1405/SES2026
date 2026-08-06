import pytest
from src_0998 import task_func

def test_task_func():
    url = "https://www.example.com/file.zip"
    target_dir = task_func(url)
    assert os.path.exists(target_dir)
    assert os.path.isdir(target_dir)
    assert os.path.exists(os.path.join(target_dir, "file.zip"))
    assert not os.path.exists(TARGET_ZIP_FILE)