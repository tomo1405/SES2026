import pytest
from src_0287 import task_func
import os
import tempfile
from collections import Counter

@pytest.fixture
def setup_files(tmpdir):
    # Create temporary files with some content
    file1 = tmpdir.join('file1.txt')
    file1.write('hello world hello')
    
    file2 = tmpdir.join('file2.txt')
    file2.write('world test')
    
    file3 = tmpdir.join('not_a_text_file.pdf')
    file3.write('some content')
    
    return str(tmpdir)

def test_task_func(setup_files):
    # Define output file path
    output_file = 'output.csv'
    
    # Call the function
    total_words = task_func(output_file, setup_files)
    
    # Check if the output file exists
    assert os.path.exists(output_file)
    
    # Read the output file and check its contents
    with open(output_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        rows = list(reader)
    
    expected_header = ['Word', 'Count']
    assert header == expected_header
    
    expected_rows = [
        ['hello', '2'],
        ['world', '2'],
        ['test', '1']
    ]
    
    # Sort rows to ensure order doesn't affect the test
    rows.sort()
    expected_rows.sort()
    
    assert rows == expected_rows
    
    # Check if the total number of words is correct
    expected_total_words = 5
    assert total_words == expected_total_words

def test_task_func_no_txt_files(setup_files):
    # Remove all .txt files
    for file in os.listdir(setup_files):
        if file.endswith('.txt'):
            os.remove(os.path.join(setup_files, file))
    
    # Define output file path
    output_file = 'output.csv'
    
    # Call the function
    total_words = task_func(output_file, setup_files)
    
    # Check if the output file exists
    assert os.path.exists(output_file)
    
    # Read the output file and check its contents
    with open(output_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        rows = list(reader)
    
    expected_header = ['Word', 'Count']
    assert header == expected_header
    
    expected_rows = []
    assert rows == expected_rows
    
    # Check if the total number of words is correct
    expected_total_words = 0
    assert total_words == expected_total_words

def test_task_func_empty_directory(setup_files):
    # Empty the directory
    for file in os.listdir(setup_files):
        os.remove(os.path.join(setup_files, file))
    
    # Define output file path
    output_file = 'output.csv'
    
    # Call the function
    total_words = task_func(output_file, setup_files)
    
    # Check if the output file exists
    assert os.path.exists(output_file)
    
    # Read the output file and check its contents
    with open(output_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        rows = list(reader)
    
    expected_header = ['Word', 'Count']
    assert header == expected_header
    
    expected_rows = []
    assert rows == expected_rows
    
    # Check if the total number of words is correct
    expected_total_words = 0
    assert total_words == expected_total_words