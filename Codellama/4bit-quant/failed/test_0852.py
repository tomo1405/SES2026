import pytest
from src_0852 import task_func

def test_task_func():
    input_string = "This is a test string"
    width = 10
    expected_output = "This was a test string"
    actual_output = task_func(input_string, width)
    assert actual_output == expected_output

def test_task_func_with_long_word():
    input_string = "This is a very long test string"
    width = 10
    expected_output = "This was a very long test string"
    actual_output = task_func(input_string, width)
    assert actual_output == expected_output

def test_task_func_with_long_word_and_width():
    input_string = "This is a very long test string"
    width = 5
    expected_output = "This was a very long test string"
    actual_output = task_func(input_string, width)
    assert actual_output == expected_output

def test_task_func_with_long_word_and_width_2():
    input_string = "This is a very long test string"
    width = 10
    expected_output = "This was a very long test string"
    actual_output = task_func(input_string, width)
    assert actual_output == expected_output

def test_task_func_with_long_word_and_width_3():
    input_string = "This is a very long test string"
    width = 15
    expected_output = "This was a very long test string"
    actual_output = task_func(input_string, width)
    assert actual_output == expected_output

def test_task_func_with_long_word_and_width_4():
    input_string = "This is a very long test string"
    width = 20
    expected_output = "This was a very long test string"
    actual_output = task_func(input_string, width)
    assert actual_output == expected_output

def test_task_func_with_long_word_and_width_5():
    input_string = "This is a very long test string"
    width = 25
    expected_output = "This was a very long test string"
    actual_output = task_func(input_string, width)
    assert actual_output == expected_output

def test_task_func_with_long_word_and_width_6():
    input_string = "This is a very long test string"
    width = 30
    expected_output = "This was a very long test string"
    actual_output = task_func(input_string, width)
    assert actual_output == expected_output

def test_task_func_with_long_word_and_width_7():
    input_string = "This is a very long test string"
    width = 35
    expected_output = "This was a very long test string"
    actual_output = task_func(input_string, width)
    assert actual_output == expected_output

def test_task_func_with_long_word_and_width_8():
    input_string = "This is a very long test string"
    width = 40
    expected_output = "This was a very long test string"
    actual_output = task_func(input_string, width)
    assert actual_output == expected_output

def test_task_func_with_long_word_and_width_9():
    input_string = "This is a very long test string"
    width = 45
    expected_output = "This was a very long test string"
    actual_output = task_func(input_string, width)
    assert actual_output == expected_output

def test_task_func_with_long_word_and_width_10():
    input_string = "This is a very long test string"
    width = 50
    expected_output = "This was a very long test string"
    actual_output = task_func(input_string, width)
    assert actual_output == expected_output