python
import os
import shutil
import pytest
from src_0381 import task_func

@pytest.fixture
def temp_dir(tmpdir):
    temp_dir = tmpdir.mkdir("temp")
    temp_dir.join("file1.txt").write("content1")
    temp_dir.join("file2.txt").write("content2")
    temp_dir.join("file3.txt").write("content3")
    return temp_dir

def test_task_func(temp_dir):
    task_func(temp_dir)
    assert os.path.exists(os.path.join(temp_dir, "txt"))
    assert os.path.exists(os.path.join(temp_dir, "txt", "file1.txt"))
    assert os.path.exists(os.path.join(temp_dir, "txt", "file2.txt"))
    assert os.path.exists(os.path.join(temp_dir, "txt", "file3.txt"))
    assert not os.path.exists(os.path.join(temp_dir, "file1.txt"))
    assert not os.path.exists(os.path.join(temp_dir, "file2.txt"))
    assert not os.path.exists(os.path.join(temp_dir, "file3.txt"))