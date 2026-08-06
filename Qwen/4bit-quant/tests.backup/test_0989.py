import pytest
from src_0989 import task_func

def test_task_func_with_valid_predicates():
    # Setup
    dir_path = "/tmp/test_dir"
    os.makedirs(dir_path, exist_ok=True)
    file_path = os.path.join(dir_path, "testfile.txt")
    open(file_path, 'a').close()
    predicates = ["is_file", "is_dir"]

    # Execute
    result = task_func(dir_path, predicates)

    # Assert
    assert isinstance(result, dict)
    assert len(result) == 1
    assert "testfile.txt" in result
    assert result["testfile.txt"]["is_file"] is True
    assert result["testfile.txt"]["is_dir"] is False

    # Cleanup
    os.remove(file_path)
    os.rmdir(dir_path)

def test_task_func_with_invalid_predicates():
    # Setup
    dir_path = "/tmp/test_dir"
    os.makedirs(dir_path, exist_ok=True)
    file_path = os.path.join(dir_path, "testfile.txt")
    open(file_path, 'a').close()
    predicates = ["invalid_predicate"]

    # Execute and Assert
    with pytest.raises(ValueError, match="No valid predicates provided."):
        task_func(dir_path, predicates)

    # Cleanup
    os.remove(file_path)
    os.rmdir(dir_path)

def test_task_func_with_non_existent_directory():
    # Setup
    dir_path = "/tmp/non_existent_dir"
    predicates = ["is_file"]

    # Execute and Assert
    with pytest.raises(FileNotFoundError, match="The directory /tmp/non_existent_dir does not exist or is not a directory."):
        task_func(dir_path, predicates)

def test_task_func_with_empty_directory():
    # Setup
    dir_path = "/tmp/empty_dir"
    os.makedirs(dir_path, exist_ok=True)
    predicates = ["is_file"]

    # Execute
    result = task_func(dir_path, predicates)

    # Assert
    assert isinstance(result, dict)
    assert len(result) == 0

    # Cleanup
    os.rmdir(dir_path)

def test_task_func_with_special_characters():
    # Setup
    dir_path = "/tmp/test_dir"
    os.makedirs(dir_path, exist_ok=True)
    file_path = os.path.join(dir_path, "test@file.txt")
    open(file_path, 'a').close()
    predicates = ["has_special_chars"]

    # Execute
    result = task_func(dir_path, predicates)

    # Assert
    assert isinstance(result, dict)
    assert len(result) == 1
    assert "test@file.txt" in result
    assert result["test@file.txt"]["has_special_chars"] is True

    # Cleanup
    os.remove(file_path)
    os.rmdir(dir_path)

def test_task_func_with_numbers():
    # Setup
    dir_path = "/tmp/test_dir"
    os.makedirs(dir_path, exist_ok=True)
    file_path = os.path.join(dir_path, "testfile1.txt")
    open(file_path, 'a').close()
    predicates = ["has_numbers"]

    # Execute
    result = task_func(dir_path, predicates)

    # Assert
    assert isinstance(result, dict)
    assert len(result) == 1
    assert "testfile1.txt" in result
    assert result["testfile1.txt"]["has_numbers"] is True

    # Cleanup
    os.remove(file_path)
    os.rmdir(dir_path)