import pytest
from src_0868 import task_func

def test_task_func_no_punctuation():
    text1 = "Hello, world!"
    text2 = "Python is great."
    expected_output = ("Hello world", "Python is great")
    assert task_func(text1, text2) == expected_output

def test_task_func_with_special_characters():
    text1 = "Hello!!!"
    text2 = "Python@#"
    expected_output = ("Hello", "Python")
    assert task_func(text1, text2) == expected_output

def test_task_func_empty_strings():
    text1 = ""
    text2 = ""
    expected_output = ("", "")
    assert task_func(text1, text2) == expected_output

def test_task_func_no_change_needed():
    text1 = "NoPunctuationHere"
    text2 = "AnotherExample"
    expected_output = ("NoPunctuationHere", "AnotherExample")
    assert task_func(text1, text2) == expected_output

def test_task_func_mixed_case():
    text1 = "MiXeD CaSe!"
    text2 = "pUnCtUaTiOn"
    expected_output = ("MiXeD CaSe", "pUnCtUaTiOn")
    assert task_func(text1, text2) == expected_output