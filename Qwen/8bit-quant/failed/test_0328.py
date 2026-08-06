import pytest
from src_0328 import task_func

def test_task_func_with_empty_file(tmp_path):
    # Create an empty CSV file
    empty_file = tmp_path / "empty.csv"
    empty_file.touch()

    # Call the function with the path to the empty file
    result = task_func(str(empty_file))

    # Assert that the result is an empty dictionary
    assert result == {}

def test_task_func_with_single_row(tmp_path):
    # Create a CSV file with a single row
    single_row_file = tmp_path / "single_row.csv"
    single_row_file.write_text("Hello, World!")

    # Call the function with the path to the single row file
    result = task_func(str(single_row_file))

    # Expected matches: ['Hello', ',', 'World', '!']
    expected_result = {'Hello': 1, ',': 1, 'World': 1, '!': 1}
    assert result == expected_result

def test_task_func_with_multiple_rows(tmp_path):
    # Create a CSV file with multiple rows
    multiple_rows_file = tmp_path / "multiple_rows.csv"
    multiple_rows_file.write_text("Hello, World!\nPython is great!")

    # Call the function with the path to the multiple rows file
    result = task_func(str(multiple_rows_file))

    # Expected matches: ['Hello', ',', 'World', '!', 'Python', 'is', 'great', '!']
    expected_result = {'Hello': 1, ',': 1, 'World': 1, '!': 2, 'Python': 1, 'is': 1, 'great': 1}
    assert result == expected_result

def test_task_func_with_custom_regex(tmp_path):
    # Create a CSV file with a single row
    custom_regex_file = tmp_path / "custom_regex.csv"
    custom_regex_file.write_text("Hello, World!")

    # Define a custom regex pattern
    custom_pattern = r'\b\w+\b'

    # Call the function with the path to the custom regex file and the custom pattern
    result = task_func(str(custom_regex_file), regex_pattern=custom_pattern)

    # Expected matches: ['Hello', 'World']
    expected_result = {'Hello': 1, 'World': 1}
    assert result == expected_result

def test_task_func_with_nonexistent_file():
    # Call the function with a non-existent file path
    with pytest.raises(FileNotFoundError):
        task_func('non_existent_file.csv')