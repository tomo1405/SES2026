import pytest
from src_0097 import task_func

def test_task_func_with_default_delimiter(tmp_path):
    # Create a temporary CSV file
    csv_content = "word1,word2,word3\nword1,word2,word4"
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(csv_content)

    # Expected output: [('word1', 2), ('word2', 2), ('word3', 1), ('word4', 1)]
    expected_output = [('word1', 2), ('word2', 2), ('word3', 1), ('word4', 1)]

    assert task_func(str(csv_file), ',') == expected_output

def test_task_func_with_custom_delimiter(tmp_path):
    # Create a temporary CSV file with a custom delimiter
    csv_content = "word1;word2;word3\nword1;word2;word4"
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(csv_content)

    # Expected output: [('word1', 2), ('word2', 2), ('word3', 1), ('word4', 1)]
    expected_output = [('word1', 2), ('word2', 2), ('word3', 1), ('word4', 1)]

    assert task_func(str(csv_file), ';') == expected_output

def test_task_func_with_empty_file(tmp_path):
    # Create an empty CSV file
    csv_file = tmp_path / "empty.csv"
    csv_file.write_text("")

    # Expected output: []
    expected_output = []

    assert task_func(str(csv_file), ',') == expected_output

def test_task_func_with_single_word(tmp_path):
    # Create a CSV file with a single word
    csv_content = "singleword"
    csv_file = tmp_path / "single.csv"
    csv_file.write_text(csv_content)

    # Expected output: [('singleword', 1)]
    expected_output = [('singleword', 1)]

    assert task_func(str(csv_file), ',') == expected_output

def test_task_func_with_multiple_lines(tmp_path):
    # Create a CSV file with multiple lines
    csv_content = "word1,word2\nword1,word3\nword1,word4"
    csv_file = tmp_path / "multiple.csv"
    csv_file.write_text(csv_content)

    # Expected output: [('word1', 3), ('word2', 1), ('word3', 1), ('word4', 1)]
    expected_output = [('word1', 3), ('word2', 1), ('word3', 1), ('word4', 1)]

    assert task_func(str(csv_file), ',') == expected_output