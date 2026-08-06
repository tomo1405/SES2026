import pytest
from src_1110 import task_func
from nltk import word_tokenize

def test_task_func_file_not_found():
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func('non_existent_file.txt')
    assert str(excinfo.value) == "File not found: non_existent_file.txt"

def test_task_func_with_valid_file(tmp_path):
    # Create a temporary file and write some content to it
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "test_file.txt"
    p.write_text("Hello world! This is a test.")

    # Expected tokens using word_tokenize
    expected_tokens = word_tokenize("Hello world! This is a test.")

    # Call the function with the path to the temporary file
    result = task_func(str(p))

    # Assert that the result matches the expected tokens
    assert result == expected_tokens

def test_task_func_with_empty_file(tmp_path):
    # Create a temporary file and leave it empty
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "empty_file.txt"
    p.touch()

    # Expected tokens for an empty file
    expected_tokens = []

    # Call the function with the path to the empty file
    result = task_func(str(p))

    # Assert that the result matches the expected tokens
    assert result == expected_tokens