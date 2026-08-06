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

    # Test case 3: source directory contains no files
    os.makedirs("empty_directory")
    moved_files = task_func("empty_directory", "target_directory")
    assert moved_files == 0

    # Test case 4: source directory contains files
    os.makedirs("source_directory")
    with open("source_directory/file1.txt", "w") as f:
        f.write("test")
    with open("source_directory/file2.docx", "w") as f:
        f.write("test")
    with open("source_directory/file3.xlsx", "w") as f:
        f.write("test")
    with open("source_directory/file4.csv", "w") as f:
        f.write("test")
    moved_files = task_func("source_directory", "target_directory")
    assert moved_files == 4

    # Test case 5: target directory already contains files
    os.makedirs("target_directory")
    with open("target_directory/file1.txt", "w") as f:
        f.write("test")
    with open("target_directory/file2.docx", "w") as f:
        f.write("test")
    with open("target_directory/file3.xlsx", "w") as f:
        f.write("test")
    with open("target_directory/file4.csv", "w") as f:
        f.write("test")
    moved_files = task_func("source_directory", "target_directory")
    assert moved_files == 4

    # Test case 6: source directory contains files with the same name
    os.makedirs("source_directory/subdirectory")
    with open("source_directory/subdirectory/file1.txt", "w") as f:
        f.write("test")
    with open("source_directory/subdirectory/file2.docx", "w") as f:
        f.write("test")
    with open("source_directory/subdirectory/file3.xlsx", "w") as f:
        f.write("test")
    with open("source_directory/subdirectory/file4.csv", "w") as f:
        f.write("test")
    moved_files = task_func("source_directory", "target_directory")
    assert moved_files == 8

    # Test case 7: source directory contains files with the same name and different extensions
    os.makedirs("source_directory/subdirectory2")
    with open("source_directory/subdirectory2/file1.txt", "w") as f:
        f.write("test")
    with open("source_directory/subdirectory2/file2.docx", "w") as f:
        f.write("test")
    with open("source_directory/subdirectory2/file3.xlsx", "w") as f:
        f.write("test")
    with open("source_directory/subdirectory2/file4.csv", "w") as f:
        f.write("test")
    with open("source_directory/subdirectory2/file5.jpg", "w") as f:
        f.write("test")
    moved_files = task_func("source_directory", "target_directory")
    assert moved_files == 12