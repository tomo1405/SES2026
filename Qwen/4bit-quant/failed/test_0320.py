import pytest
from src_0320 import task_func
import matplotlib.pyplot as plt
from nltk.probability import FreqDist

def test_task_func():
    example_str = "This is a test [string] with some repeated words and more words"
    ax, top_n_words = task_func(example_str, top_n=5)
    
    # Check if the returned object is a matplotlib AxesSubplot
    assert isinstance(ax, plt.Axes), "The first return value should be a matplotlib AxesSubplot"
    
    # Check if the top_n_words dictionary has the correct number of items
    assert len(top_n_words) == 5, "The top_n_words dictionary should have 5 items"
    
    # Check if the top_n_words dictionary contains the expected words
    expected_words = {'words': 2, 'and': 1, 'some': 1, 'test': 1, 'with': 1}
    assert top_n_words == expected_words, "The top_n_words dictionary does not match the expected output"

def test_task_func_with_less_than_top_n_unique_words():
    example_str = "This is a test string"
    ax, top_n_words = task_func(example_str, top_n=10)
    
    # Check if the returned object is a matplotlib AxesSubplot
    assert isinstance(ax, plt.Axes), "The first return value should be a matplotlib AxesSubplot"
    
    # Check if the top_n_words dictionary has the correct number of items
    assert len(top_n_words) == 4, "The top_n_words dictionary should have 4 items"
    
    # Check if the top_n_words dictionary contains the expected words
    expected_words = {'This': 1, 'is': 1, 'a': 1, 'test': 1, 'string': 1}
    assert top_n_words == expected_words, "The top_n_words dictionary does not match the expected output"

def test_task_func_with_no_words():
    example_str = "No words here"
    ax, top_n_words = task_func(example_str, top_n=5)
    
    # Check if the returned object is a matplotlib AxesSubplot
    assert isinstance(ax, plt.Axes), "The first return value should be a matplotlib AxesSubplot"
    
    # Check if the top_n_words dictionary is empty
    assert len(top_n_words) == 0, "The top_n_words dictionary should be empty"
    
    # Check if the top_n_words dictionary is indeed empty
    assert top_n_words == {}, "The top_n_words dictionary does not match the expected output"

def test_task_func_with_empty_string():
    example_str = ""
    ax, top_n_words = task_func(example_str, top_n=5)
    
    # Check if the returned object is a matplotlib AxesSubplot
    assert isinstance(ax, plt.Axes), "The first return value should be a matplotlib AxesSubplot"
    
    # Check if the top_n_words dictionary is empty
    assert len(top_n_words) == 0, "The top_n_words dictionary should be empty"
    
    # Check if the top_n_words dictionary is indeed empty
    assert top_n_words == {}, "The top_n_words dictionary does not match the expected output"