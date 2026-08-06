import pytest
from src_0097 import task_func
from collections import Counter

def test_task_func_with_simple_csv(tmp_path):
    # Create a temporary CSV file
    csv_content = "apple,banana,apple\norange,banana,grape"
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(csv_content)

    # Define the expected output
    expected_output = [('apple', 2), ('banana', 2), ('orange', 1), ('grape', 1)]

    # Call the function and check the result
    result = task_func(str(csv_file), ',')
    assert result == expected_output

def test_task_func_with_tab_delimiter(tmp_path):
    # Create a temporary CSV file with tab delimiter
    csv_content = "apple\tbanana\tapple\norange\tbanana\tgrape"
    csv_file = tmp_path / "test.tsv"
    csv_file.write_text(csv_content)

    # Define the expected output
    expected_output = [('apple', 2), ('banana', 2), ('orange', 1), ('grape', 1)]

    # Call the function and check the result
    result = task_func(str(csv_file), '\t')
    assert result == expected_output

def test_task_func_with_single_word(tmp_path):
    # Create a temporary CSV file with a single word
    csv_content = "apple"
    csv_file = tmp_path / "single_word.csv"
    csv_file.write_text(csv_content)

    # Define the expected output
    expected_output = [('apple', 1)]

    # Call the function and check the result
    result = task_func(str(csv_file), ',')
    assert result == expected_output

def test_task_func_with_empty_file(tmp_path):
    # Create an empty temporary CSV file
    csv_file = tmp_path / "empty.csv"
    csv_file.write_text("")

    # Define the expected output
    expected_output = []

    # Call the function and check the result
    result = task_func(str(csv_file), ',')
    assert result == expected_output

def test_task_func_with_no_words(tmp_path):
    # Create a temporary CSV file with no words
    csv_content = ",,"
    csv_file = tmp_path / "no_words.csv"
    csv_file.write_text(csv_content)

    # Define the expected output
    expected_output = [('', 3)]

    # Call the function and check the result
    result = task_func(str(csv_file), ',')
    assert result == expected_output