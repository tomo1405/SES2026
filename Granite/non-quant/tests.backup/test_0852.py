import pytest
from src_0852 import task_func

def test_task_func():
    input_string = "This is a test string.\nIt has multiple lines."
    width = 20
    expected_output = "This was a test string.\nIt was multiple lines."
    
    actual_output = task_func(input_string, width)
    
    assert actual_output == expected_output