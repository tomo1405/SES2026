import pytest
from src_1086 import task_func
from collections import Counter
import matplotlib.pyplot as plt
import io
import sys

# Mocking the plt.subplots to capture the plot
class MockAxes:
    def bar(self, *args, **kwargs):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

class MockSubplots:
    def __call__(self):
        return None, MockAxes()

@pytest.fixture
def mock_plt(mocker):
    mocker.patch('matplotlib.pyplot.subplots', new_callable=MockSubplots)
    return plt

def test_task_func_no_punctuation():
    text = "Hello world! Hello everyone."
    expected_output = [('hello', 2), ('world', 1), ('everyone', 1)]
    result, _ = task_func(text)
    assert result == expected_output

def test_task_func_empty_string():
    text = ""
    expected_output = []
    result, _ = task_func(text)
    assert result == expected_output

def test_task_func_single_word():
    text = "Test"
    expected_output = [('test', 1)]
    result, _ = task_func(text)
    assert result == expected_output

def test_task_func_multiple_words_with_same_count():
    text = "One two three two one"
    expected_output = [('one', 2), ('two', 2), ('three', 1)]
    result, _ = task_func(text)
    assert result == expected_output

def test_task_func_plot(mock_plt):
    text = "Plot this plot"
    _, ax = task_func(text)
    assert isinstance(ax, MockAxes)

def test_task_func_punctuation_handling():
    text = "Punctuation, should be; ignored!"
    expected_output = [('punctuation', 1), ('should', 1), ('be', 1), ('ignored', 1)]
    result, _ = task_func(text)
    assert result == expected_output

def test_task_func_case_insensitivity():
    text = "Case CASE case"
    expected_output = [('case', 3)]
    result, _ = task_func(text)
    assert result == expected_output