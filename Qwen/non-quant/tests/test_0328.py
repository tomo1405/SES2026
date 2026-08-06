import pytest
from src_0328 import task_func
from collections import Counter

def test_task_func_with_empty_file(tmp_path):
    empty_file = tmp_path / "empty.csv"
    empty_file.write_text("")
    
    result = task_func(str(empty_file))
    assert result == {}

def test_task_func_with_single_row(tmp_path):
    single_row_file = tmp_path / "single_row.csv"
    single_row_file.write_text("Hello, world!")
    
    result = task_func(str(single_row_file))
    expected_counts = Counter(['Hello', ',', 'world', '!'])
    assert result == dict(expected_counts)

def test_task_func_with_multiple_rows(tmp_path):
    multiple_rows_file = tmp_path / "multiple_rows.csv"
    multiple_rows_file.write_text("Hello, world!\nPython is great.\n")
    
    result = task_func(str(multiple_rows_file))
    expected_counts = Counter(['Hello', ',', 'world', '!', 'Python', 'is', 'great', '.'])
    assert result == dict(expected_counts)

def test_task_func_with_custom_regex(tmp_path):
    custom_regex_file = tmp_path / "custom_regex.csv"
    custom_regex_file.write_text("Hello, world!")
    
    result = task_func(str(custom_regex_file), r'\b\w+\b')
    expected_counts = Counter(['Hello', 'world'])
    assert result == dict(expected_counts)

def test_task_func_with_special_characters(tmp_path):
    special_characters_file = tmp_path / "special_characters.csv"
    special_characters_file.write_text("Hello, @world! #Python &is* great.")
    
    result = task_func(str(special_characters_file))
    expected_counts = Counter(['Hello', ',', '@', 'world', '!', '#', 'Python', '&', 'is', '*', 'great', '.'])
    assert result == dict(expected_counts)