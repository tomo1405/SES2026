import pytest
from src_0813 import task_func

def test_task_func():
    # Test that the function returns the expected tar path
    tar_path = task_func()
    assert tar_path == "C:\\SomeDir\\archive.tar"

    # Test that the function skips files with permission errors
    with pytest.raises(PermissionError):
        task_func(directory="C:\\SomeDir\\", file_pattern=r"(?<!Distillr)\\\\AcroTray\.exe")