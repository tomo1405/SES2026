import pytest
from src_0963 import task_func


def test_task_func():
    source_directory = "tests/data/source"
    target_directory = "tests/data/target"

    moved_files = task_func(source_directory, target_directory)

    assert moved_files == 4

    for extension in [".txt", ".docx", ".xlsx", ".csv"]:
        filepaths = glob.glob(
            os.path.join(source_directory, "**", "*" + extension), recursive=True
        )
        for filepath in filepaths:
            filename = Path(filepath).name
            stem = Path(filepath).stem
            target_filepath = os.path.join(target_directory, filename)

            assert os.path.exists(target_filepath)

            count = 1
            while os.path.exists(target_filepath):
                new_filename = f"{stem}-{count}{extension}"
                target_filepath = os.path.join(target_directory, new_filename)
                count += 1

            assert os.path.exists(target_filepath)

            shutil.move(filepath, target_filepath)
            moved_files += 1

    assert moved_files == 4