import os

from src_0766 import task_func


def test_task_func_with_valid_input():
    kwargs = {"file1.txt": "file1 content", "file2.txt": "file2 content"}
    target_dir = "non_none_files"
    copied_files = task_func(kwargs, target_dir)
    assert len(copied_files) == 2
    assert os.path.exists(copied_files[0])
    assert os.path.exists(copied_files[1])
    assert os.path.isfile(copied_files[0])
    assert os.path.isfile(copied_files[1])
    assert os.path.getsize(copied_files[0]) > 0
    assert os.path.getsize(copied_files[1]) > 0
    assert os.path.getsize(copied_files[0]) == len(kwargs["file1.txt"])
    assert os.path.getsize(copied_files[1]) == len(kwargs["file2.txt"])
    assert os.path.getmtime(copied_files[0]) > 0
    assert os.path.getmtime(copied_files[1]) > 0
    assert os.path.getmtime(copied_files[0]) == os.path.getmtime(kwargs["file1.txt"])
    assert os.path.getmtime(copied_files[1]) == os.path.getmtime(kwargs["file2.txt"])


def test_task_func_with_invalid_input():
    kwargs = {"file1.txt": "file1 content", "file2.txt": None}
    target_dir = "non_none_files"
    copied_files = task_func(kwargs, target_dir)
    assert len(copied_files) == 1
    assert os.path.exists(copied_files[0])
    assert os.path.isfile(copied_files[0])
    assert os.path.getsize(copied_files[0]) > 0
    assert os.path.getsize(copied_files[0]) == len(kwargs["file1.txt"])
    assert os.path.getmtime(copied_files[0]) > 0
    assert os.path.getmtime(copied_files[0]) == os.path.getmtime(kwargs["file1.txt"])


def test_task_func_with_empty_input():
    kwargs = {}
    target_dir = "non_none_files"
    copied_files = task_func(kwargs, target_dir)
    assert len(copied_files) == 0


def test_task_func_with_invalid_target_dir():
    kwargs = {"file1.txt": "file1 content", "file2.txt": "file2 content"}
    target_dir = "non_existent_dir"
    copied_files = task_func(kwargs, target_dir)
    assert len(copied_files) == 0