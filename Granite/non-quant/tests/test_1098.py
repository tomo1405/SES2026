import pytest
from src_1098 import task_func

def test_task_func():
    assert task_func("This is a test.") == "test"
    assert task_func("This is another test!") == "another test"
    assert task_func("This is a test... And this is another test?") == "test and this is another test"
    assert task_func("This is a test. This is another test.") == "test this is another test"
    assert task_func("This is a test. This is another test... And this is a third test?") == "test this is another test and this is a third test"

def test_task_func_with_urls():
    assert task_func("This is a test. Here is a URL: https://www.example.com") == "test here is a url"
    assert task_func("This is a test. Here are two URLs: https://www.example.com and https://www.google.com") == "test here are two urls and"
    assert task_func("This is a test. Here is a URL: https://www.example.com. Here is another URL: https://www.google.com") == "test here is a url here is another url"

def test_task_func_with_punctuation():
    assert task_func("This is a test!") == "test"
    assert task_func("This is a test...") == "test"
    assert task_func("This is a test?") == "test"
    assert task_func("This is a test. This is another test!") == "test this is another test"
    assert task_func("This is a test. This is another test... And this is a third test?") == "test this is another test and this is a third test"

def test_task_func_with_stopwords():
    assert task_func("This is a test. This is another test.") == "test this is another test"
    assert task_func("This is a test. This is another test. This is a stopword.") == "test this is another test"
    assert task_func("This is a test. This is another test. This is a stopword. This is a stopword.") == "test this is another test"
    assert task_func("This is a test. This is another test. This is a stopword. This is a stopword. This is a stopword.") == "test this is another test"

def test_task_func_with_empty_string():
    assert task_func("") == ""

def test_task_func_with_only_punctuation():
    assert task_func("!@#$%^&*()_+") == ""

def test_task_func_with_only_stopwords():
    assert task_func("this is a test. this is another test. this is a stopword. this is a stopword. this is a stopword.") == ""