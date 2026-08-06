import pytest
from src_1086 import task_func
from collections import Counter
import matplotlib.pyplot as plt
import io
import sys

# Mocking matplotlib to capture plot output
@pytest.fixture
def mock_plot():
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    yield
    sys.stdout = old_stdout

def test_task_func_with_text(mock_plot):
    text = "Hello world! Hello everyone. Welcome to the world of Python."
    expected_most_common_words = [('hello', 2), ('world', 2), ('everyone', 1), ('welcome', 1), ('to', 1), ('the', 1), ('of', 1), ('python', 1)]
    
    most_common_words, ax = task_func(text)
    
    assert most_common_words == expected_most_common_words
    assert isinstance(ax, plt.Axes)

def test_task_func_with_empty_text(mock_plot):
    text = ""
    expected_most_common_words = []
    
    most_common_words, ax = task_func(text)
    
    assert most_common_words == expected_most_common_words
    assert isinstance(ax, plt.Axes)

def test_task_func_with_no_words(mock_plot):
    text = "!!!"
    expected_most_common_words = []
    
    most_common_words, ax = task_func(text)
    
    assert most_common_words == expected_most_common_words
    assert isinstance(ax, plt.Axes)