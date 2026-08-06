import pytest
from src_0964 import task_func

def test_task_func():
    source_directory = "path/to/source/directory"
    target_directory = "path/to/target/directory"
    zip_name = "test_zip"

    # Test that the function raises an error if the source directory does not exist
    with pytest.raises(OSError):
        task_func("invalid_source_directory", target_directory, zip_name)

    # Test that the function creates the target directory if it does not exist
    task_func(source_directory, "invalid_target_directory", zip_name)
    assert os.path.exists("invalid_target_directory")

    # Test that the function creates a zip file with the correct name and contents
    task_func(source_directory, target_directory, zip_name)
    assert os.path.exists(os.path.join(target_directory, f"{zip_name}.zip"))
    with zipfile.ZipFile(os.path.join(target_directory, f"{zip_name}.zip"), "r") as zipf:
        assert zipf.namelist() == ["file1.txt", "file2.docx", "file3.xlsx", "file4.csv"]

    # Test that the function returns the absolute path of the zip file
    assert task_func(source_directory, target_directory, zip_name) == os.path.abspath(os.path.join(target_directory, f"{zip_name}.zip"))