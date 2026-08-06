import pytest
from src_1096 import task_func
from io import StringIO
import os

@pytest.fixture
def setup_and_teardown(tmpdir):
    input_text = "This is a test $word with some $punctuation! and $validWord."
    output_filename = str(tmpdir / "output.txt")
    yield input_text, output_filename
    if os.path.exists(output_filename):
        os.remove(output_filename)

def test_task_func(setup_and_teardown):
    input_text, output_filename = setup_and_teardown
    result = task_func(input_text, output_filename)
    
    assert os.path.exists(output_filename)
    assert os.path.abspath(output_filename) == result
    
    with open(output_filename, 'r') as file:
        content = file.read().strip()
    
    expected_output = "$word\n$validWord"
    assert content == expected_output

def test_task_func_no_dollar_words(setup_and_teardown):
    input_text, output_filename = setup_and_teardown
    input_text = "No dollar words here!"
    task_func(input_text, output_filename)
    
    with open(output_filename, 'r') as file:
        content = file.read().strip()
    
    assert content == ""

def test_task_func_empty_input(setup_and_teardown):
    input_text, output_filename = setup_and_teardown
    input_text = ""
    task_func(input_text, output_filename)
    
    with open(output_filename, 'r') as file:
        content = file.read().strip()
    
    assert content == ""

def test_task_func_only_punctuation(setup_and_teardown):
    input_text, output_filename = setup_and_teardown
    input_text = "$$$!!!"
    task_func(input_text, output_filename)
    
    with open(output_filename, 'r') as file:
        content = file.read().strip()
    
    assert content == ""