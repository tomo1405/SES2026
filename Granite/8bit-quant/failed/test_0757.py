import pytest
from src_0757 import task_func
from pathlib import Path
import shutil

def test_task_func():
    source_dir = "source_directory"
    target_dir = "target_directory"
    extensions = [".txt", ".csv"]

    with pytest.raises(ValueError) as exc_info:
        task_func(source_dir, target_dir, extensions)
    assert "source_dir does not exist." in str(exc_info.value)

    with pytest.raises(ValueError) as exc_info:
        task_func("source_directory", target_dir, extensions)
    assert "target_dir does not exist." in str(exc_info.value)

    count = task_func("source_directory", "target_directory", extensions)
    assert count == len(extensions) * 2

    for extension in extensions:
        source_files = list(Path(source_dir).glob(f'*{extension}'))
        target_files = list(Path(target_dir).glob(f'*{extension}'))
        assert len(source_files) == len(target_files)