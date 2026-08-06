import os
import shutil

from src_0780 import task_func


def test_task_func_directory_not_exists():
    directory = "/nonexistent/directory"
    result, errors = task_func(directory)
    assert result is None
    assert len(errors) == 1
    assert errors[0] == f"Directory does not exist: {directory}"

def test_task_func_permission_error():
    # Mocking a permission error by setting up a read-only directory
    directory = "/tmp/test_dir"
    os.makedirs(directory, mode=0o444)
    try:
        result, errors = task_func(directory)
        assert result == "/fake/backup/path"
        assert len(errors) == 1
        assert "Permission denied" in errors[0]
    finally:
        os.chmod(directory, 0o777)
        shutil.rmtree(directory)

def test_task_func_success():
    # Create a temporary directory and some files to simulate a real directory
    directory = "/tmp/test_dir"
    os.makedirs(directory)
    with open(os.path.join(directory, "file1.txt"), "w") as f:
        f.write("content")
    with open(os.path.join(directory, "file2.txt"), "w") as f:
        f.write("content")

    result, errors = task_func(directory)
    assert result == "/fake/backup/path"
    assert len(errors) == 0
    assert os.path.exists(result)
    assert os.path.isdir(result)
    assert os.path.exists(os.path.join(result, os.path.basename(directory)))
    assert os.path.isdir(os.path.join(result, os.path.basename(directory)))
    assert os.path.exists(os.path.join(directory, "file1.txt"))
    assert os.path.exists(os.path.join(directory, "file2.txt"))

    # Clean up
    shutil.rmtree(directory)
    shutil.rmtree(result)