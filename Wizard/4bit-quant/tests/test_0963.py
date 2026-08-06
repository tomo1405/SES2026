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
    moved_files = task_func("source_directory", "nonexistent_directory")
    assert moved_files == 0

    # Test case 3: source directory contains files with different extensions
    source_directory = "source_directory"
    target_directory = "target_directory"
    os.makedirs(source_directory, exist_ok=True)
    os.makedirs(target_directory, exist_ok=True)
    with open(os.path.join(source_directory, "file1.txt"), "w") as f:
        f.write("test")
    with open(os.path.join(source_directory, "file2.docx"), "w") as f:
        f.write("test")
    with open(os.path.join(source_directory, "file3.xlsx"), "w") as f:
        f.write("test")
    with open(os.path.join(source_directory, "file4.csv"), "w") as f:
        f.write("test")
    moved_files = task_func(source_directory, target_directory)
    assert moved_files == 4
    assert os.path.exists(os.path.join(target_directory, "file1.txt"))
    assert os.path.exists(os.path.join(target_directory, "file2.docx"))
    assert os.path.exists(os.path.join(target_directory, "file3.xlsx"))
    assert os.path.exists(os.path.join(target_directory, "file4.csv"))

    # Test case 4: source directory contains files with the same extension
    os.remove(os.path.join(source_directory, "file1.txt"))
    with open(os.path.join(source_directory, "file1.txt"), "w") as f:
        f.write("test")
    moved_files = task_func(source_directory, target_directory)
    assert moved_files == 5
    assert os.path.exists(os.path.join(target_directory, "file1-1.txt"))
    assert os.path.exists(os.path.join(target_directory, "file2.docx"))
    assert os.path.exists(os.path.join(target_directory, "file3.xlsx"))
    assert os.path.exists(os.path.join(target_directory, "file4.csv"))
    assert os.path.exists(os.path.join(target_directory, "file1-2.txt"))

    # Test case 5: source directory contains files with the same name
    os.remove(os.path.join(source_directory, "file1-1.txt"))
    moved_files = task_func(source_directory, target_directory)
    assert moved_files == 6
    assert os.path.exists(os.path.join(target_directory, "file1-1.txt"))
    assert os.path.exists(os.path.join(target_directory, "file2.docx"))
    assert os.path.exists(os.path.join(target_directory, "file3.xlsx"))
    assert os.path.exists(os.path.join(target_directory, "file4.csv"))
    assert os.path.exists(os.path.join(target_directory, "file1-2.txt"))
    assert os.path.exists(os.path.join(target_directory, "file1-3.txt"))