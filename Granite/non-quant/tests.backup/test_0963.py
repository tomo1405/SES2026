import os
from pathlib import Path
import glob
import shutil
from tempfile import TemporaryDirectory

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
    with TemporaryDirectory() as temp_dir:
        source_dir = os.path.join(temp_dir, "source")
        target_dir = os.path.join(temp_dir, "target")
        os.makedirs(source_dir)
        with open(os.path.join(source_dir, "test.txt"), "w") as f:
            f.write("Test file")
        moved_files = task_func(source_dir, target_dir)
        assert moved_files == 1
        assert os.path.exists(os.path.join(target_dir, "test.txt"))

def test_task_func_with_existing_file():
    with TemporaryDirectory() as temp_dir:
        source_dir = os.path.join(temp_dir, "source")
        target_dir = os.path.join(temp_dir, "target")
        os.makedirs(source_dir)
        with open(os.path.join(source_dir, "test.txt"), "w") as f:
            f.write("Test file")
        with open(os.path.join(target_dir, "test.txt"), "w") as f:
            f.write("Existing file")
        moved_files = task_func(source_dir, target_dir)
        assert moved_files == 1
        assert os.path.exists(os.path.join(target_dir, "test-1.txt"))

def test_task_func_with_non_existing_source_dir():
    with TemporaryDirectory() as temp_dir:
        source_dir = os.path.join(temp_dir, "source")
        target_dir = os.path.join(temp_dir, "target")
        moved_files = task_func(source_dir, target_dir)
        assert moved_files == 0

def test_task_func_with_non_existing_target_dir():
    with TemporaryDirectory() as temp_dir:
        source_dir = os.path.join(temp_dir, "source")
        target_dir = os.path.join(temp_dir, "target")
        os.makedirs(source_dir)
        with open(os.path.join(source_dir, "test.txt"), "w") as f:
            f.write("Test file")
        moved_files = task_func(source_dir, target_dir)
        assert moved_files == 1
        assert os.path.exists(os.path.join(target_dir, "test.txt"))