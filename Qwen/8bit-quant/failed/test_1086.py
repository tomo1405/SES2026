import pytest
from src_1086 import task_func
import re
from collections import Counter
import matplotlib.pyplot as plt
import io
import sys

# Mocking the plot function to capture output
class MockPlot:
    def bar(self, *args, **kwargs):
        pass

@pytest.fixture
def mock_plt(monkeypatch):
    monkeypatch.setattr(plt, 'subplots', lambda: (None, MockPlot()))

def test_task_func_no_punctuation():
    text = "Hello world! Hello everyone."
    expected_output = [('hello', 2), ('world', 1), ('everyone', 1)]
    assert task_func(text)[0] == expected_output

def test_task_func_empty_text(mock_plt):
    text = ""
    assert task_func(text)[0] == []

def test_task_func_single_word(mock_plt):
    text = "Test"
    expected_output = [('test', 1)]
    assert task_func(text)[0] == expected_output

def test_task_func_multiple_words(mock_plt):
    text = "This is a test. This test is only a test."
    expected_output = [('this', 2), ('is', 2), ('a', 2), ('test', 2), ('only', 1)]
    assert task_func(text)[0] == expected_output

def test_task_func_case_insensitivity(mock_plt):
    text = "Hello hello HELLO"
    expected_output = [('hello', 3)]
    assert task_func(text)[0] == expected_output

def test_task_func_punctuation_removal(mock_plt):
    text = "Hello, world! This is a test."
    expected_output = [('hello', 1), ('world', 1), ('this', 1), ('is', 1), ('a', 1), ('test', 1)]
    assert task_func(text)[0] == expected_output

def test_task_func_plot_output(mock_plt):
    text = "Test test test"
    _, ax = task_func(text)
    assert isinstance(ax, MockPlot)