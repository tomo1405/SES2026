import pytest
from src_0956 import task_func
import numpy as np
import matplotlib.pyplot as plt
import re
from collections import Counter

def test_task_func_with_valid_input():
    mystrings = ["hello world", "foo bar"]
    text = "Hello world! Foo bar foo bar."
    ax = task_func(mystrings, text)
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)
    
    # Check if the text is processed correctly
    expected_text = "Hello_world! Foo_bar foo_bar."
    assert text == expected_text

    # Check if the word counts are correct
    word_counts = Counter(expected_text.split())
    expected_word_counts = {'Hello_world!': 1, 'Foo_bar': 2}
    assert word_counts == expected_word_counts

def test_task_func_with_empty_text():
    mystrings = ["hello world", "foo bar"]
    with pytest.raises(ValueError, match="text cannot be empty."):
        task_func(mystrings, "")

def test_task_func_with_no_matching_words():
    mystrings = ["hello world", "foo bar"]
    text = "No matching words here."
    ax = task_func(mystrings, text)
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)
    
    # Check if the word counts are correct
    word_counts = Counter(text.split())
    expected_word_counts = {'No': 1, 'matching': 1, 'words': 1, 'here.': 1}
    assert word_counts == expected_word_counts

def test_task_func_with_case_insensitive_replacement():
    mystrings = ["hello world"]
    text = "Hello World! hello world?"
    ax = task_func(mystrings, text)
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)
    
    # Check if the text is processed correctly
    expected_text = "Hello_world! Hello_world?"
    assert text == expected_text

    # Check if the word counts are correct
    word_counts = Counter(expected_text.split())
    expected_word_counts = {'Hello_world!': 1, 'Hello_world?': 1}
    assert word_counts == expected_word_counts