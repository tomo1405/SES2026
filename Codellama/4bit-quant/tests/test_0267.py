import pytest
from src_0267 import task_func

def test_task_func():
    # Test that the function returns the correct file path
    my_path = 'path/to/directory'
    file_path = task_func(my_path)
    assert file_path == os.path.join(my_path, FILE_NAME)

    # Test that the function writes the correct data to the file
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        assert header == ['File Name', 'Size']
        for row in reader:
            file_name, size = row
            assert file_name in file_sizes
            assert size == file_sizes[file_name]

    # Test that the function handles directories with no files
    my_path = 'path/to/empty/directory'
    file_path = task_func(my_path)
    assert file_path == os.path.join(my_path, FILE_NAME)
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        assert header == ['File Name', 'Size']
        assert not list(reader)

    # Test that the function handles directories with no subdirectories
    my_path = 'path/to/directory/with/no/subdirectories'
    file_path = task_func(my_path)
    assert file_path == os.path.join(my_path, FILE_NAME)
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        assert header == ['File Name', 'Size']
        for row in reader:
            file_name, size = row
            assert file_name in file_sizes
            assert size == file_sizes[file_name]