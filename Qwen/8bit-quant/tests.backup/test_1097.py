import pytest
from src_1097 import task_func
from string import punctuation
import os
import tempfile

@pytest.fixture
def temp_file():
    fd, name = tempfile.mkstemp()
    yield name
    os.close(fd)
    os.unlink(name)

def test_task_func(temp_file):
    text = "This is a $test with $multiple $words and $punctuation!"
    expected_output = [
        ["Word"],
        ["$test"],
        ["$multiple"],
        ["$words"],
        ["$punctuation"]
    ]
    
    result = task_func(text, temp_file)
    
    assert os.path.exists(result)
    assert os.path.abspath(result) == result
    
    with open(temp_file, 'r') as f:
        reader = csv.reader(f)
        output = list(reader)
    
    assert output == expected_output

def test_task_func_no_dollar_words(temp_file):
    text = "No dollar words here!"
    expected_output = [
        ["Word"]
    ]
    
    result = task_func(text, temp_file)
    
    assert os.path.exists(result)
    assert os.path.abspath(result) == result
    
    with open(temp_file, 'r') as f:
        reader = csv.reader(f)
        output = list(reader)
    
    assert output == expected_output

def test_task_func_empty_text(temp_file):
    text = ""
    expected_output = [
        ["Word"]
    ]
    
    result = task_func(text, temp_file)
    
    assert os.path.exists(result)
    assert os.path.abspath(result) == result
    
    with open(temp_file, 'r') as f:
        reader = csv.reader(f)
        output = list(reader)
    
    assert output == expected_output

def test_task_func_only_punctuation(temp_file):
    text = "$$$!!!"
    expected_output = [
        ["Word"]
    ]
    
    result = task_func(text, temp_file)
    
    assert os.path.exists(result)
    assert os.path.abspath(result) == result
    
    with open(temp_file, 'r') as f:
        reader = csv.reader(f)
        output = list(reader)
    
    assert output == expected_output