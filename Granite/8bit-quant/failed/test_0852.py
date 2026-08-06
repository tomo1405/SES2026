import pytest
from src_0852 import task_func

def test_task_func():
    input_string = "This is a test string.\nThis is another test string."
    width = 20
    expected_output = "This was a test string.\nThis was another test string."
    
    actual_output = task_func(input_string, width)
    
    assert actual_output == expected_output