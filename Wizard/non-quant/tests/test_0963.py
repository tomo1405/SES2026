python
import os
from pathlib import Path
import glob
import shutil
import pytest

def task_func(source_directory: str, target_directory: str):
    moved_files = 0

    if not os.path.exists(source_directory):
        raise FileNotFoundError("source_directory must exist.")

    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    for extension in [".txt", ".docx", ".xlsx", ".csv"]:
        filepaths = glob.glob(
            os.path.join(source_directory, "**", "*" + extension), recursive=True
        )
        for filepath in filepaths:
            filename = Path(filepath).name
            stem = Path(filepath).stem
            target_filepath = os.path.join(target_directory, filename)

            count = 1
            while os.path.exists(target_filepath):
                new_filename = f"{stem}-{count}{extension}"
                target_filepath = os.path.join(target_directory, new_filename)
                count += 1

            shutil.move(filepath, target_filepath)
            moved_files += 1

    return moved_files

def test_task_func():
    # Test case 1: source directory does not exist
    with pytest.raises(FileNotFoundError):
        task_func("nonexistent_directory", "target_directory")

    # Test case 2: target directory does not exist
    source_directory = "source_directory"
    target_directory = "nonexistent_directory"
    os.makedirs(source_directory)
    assert task_func(source_directory, target_directory) == 0

    # Test case 3: move files
    source_directory = "source_directory"
    target_directory = "target_directory"
    os.makedirs(source_directory)
    os.makedirs(target_directory)
    for i in range(10):
        with open(os.path.join(source_directory, f"file{i}.txt"), "w") as f:
            f.write("test")
    assert task_func(source_directory, target_directory) == 10

    # Test case 4: move files with existing target files
    source_directory = "source_directory"
    target_directory = "target_directory"
    os.makedirs(source_directory)
    os.makedirs(target_directory)
    for i in range(10):
        with open(os.path.join(source_directory, f"file{i}.txt"), "w") as f:
            f.write("test")
    for i in range(5):
        with open(os.path.join(target_directory, f"file{i}.txt"), "w") as f:
            f.write("test")
    assert task_func(source_directory, target_directory) == 10