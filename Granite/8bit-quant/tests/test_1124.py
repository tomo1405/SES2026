import pytest
from src_1124 import task_func

def test_task_func():
    myString = "Here are some URLs: https://www.example.com and https://www.google.com"
    expected_output = {'www.example.com': 'Not After: ...', 'www.google.com': 'Not After: ...'}
    actual_output = task_func(myString)
    assert actual_output == expected_output, "Task function returned an incorrect output"

def test_task_func_with_no_urls():
    myString = "Here are some strings without URLs"
    expected_output = {}
    actual_output = task_func(myString)
    assert actual_output == expected_output, "Task function returned an incorrect output"

def test_task_func_with_invalid_url():
    myString = "Here is an invalid URL: http://www.invalid"
    expected_output = {}
    actual_output = task_func(myString)
    assert actual_output == expected_output, "Task function returned an incorrect output"