import pytest
from src_1097 import task_func
import os
import csv
from string import punctuation

def test_task_func():
    # Test with a simple text containing dollar-prefixed words
    text = "This is a $test and another $example. $123 is a number."
    filename = "test_output.csv"
    
    # Call the function
    result = task_func(text, filename)
    
    # Check if the file was created and its path is returned correctly
    assert os.path.exists(result), f"File {result} does not exist"
    assert os.path.abspath(filename) == result
    
    # Read the CSV file to verify its contents
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    # The first row should be the header
    assert rows[0] == ["Word"]
    
    # The remaining rows should contain the dollar-prefixed words
    expected_words = ["$test", "$example"]
    actual_words = [row[0] for row in rows[1:]]
    assert actual_words == expected_words
    
    # Clean up the test file
    os.remove(filename)

def test_task_func_no_dollar_words():
    # Test with a text that does not contain any dollar-prefixed words
    text = "This is a test and another example. 123 is a number."
    filename = "test_output_empty.csv"
    
    # Call the function
    result = task_func(text, filename)
    
    # Check if the file was created and its path is returned correctly
    assert os.path.exists(result), f"File {result} does not exist"
    assert os.path.abspath(filename) == result
    
    # Read the CSV file to verify its contents
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    # The first row should be the header
    assert rows[0] == ["Word"]
    
    # The remaining rows should be empty
    assert len(rows) == 1
    
    # Clean up the test file
    os.remove(filename)

def test_task_func_only_punctuation():
    # Test with a text that contains only dollar-prefixed words with punctuation
    text = "$!@# and $%^&*."
    filename = "test_output_punctuation.csv"
    
    # Call the function
    result = task_func(text, filename)
    
    # Check if the file was created and its path is returned correctly
    assert os.path.exists(result), f"File {result} does not exist"
    assert os.path.abspath(filename) == result
    
    # Read the CSV file to verify its contents
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    # The first row should be the header
    assert rows[0] == ["Word"]
    
    # The remaining rows should be empty
    assert len(rows) == 1
    
    # Clean up the test file
    os.remove(filename)