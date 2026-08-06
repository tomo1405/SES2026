import pytest
from src_0320 import task_func
import matplotlib.pyplot as plt
from nltk.probability import FreqDist

def test_task_func():
    example_str = "This is a test [example] string with some words [and] more words."
    ax, top_n_words = task_func(example_str, top_n=5)
    
    # Check if the returned object is a matplotlib AxesSubplot
    assert isinstance(ax, plt.Axes)
    
    # Check if the top_n_words is a dictionary
    assert isinstance(top_n_words, dict)
    
    # Check if the dictionary contains the correct number of items
    assert len(top_n_words) == 5
    
    # Check if the dictionary contains the correct words and frequencies
    expected_words = {'words', 'test', 'a', 'is', 'with'}
    assert set(top_n_words.keys()) == expected_words

def test_task_func_top_n_greater_than_unique_words():
    example_str = "Single word repeated"
    ax, top_n_words = task_func(example_str, top_n=10)
    
    # Check if the returned object is a matplotlib AxesSubplot
    assert isinstance(ax, plt.Axes)
    
    # Check if the top_n_words is a dictionary
    assert isinstance(top_n_words, dict)
    
    # Check if the dictionary contains the correct number of items
    assert len(top_n_words) == 1
    
    # Check if the dictionary contains the correct word and frequency
    expected_word = 'word'
    assert list(top_n_words.keys())[0] == expected_word

def test_task_func_no_words():
    example_str = "No words here!"
    ax, top_n_words = task_func(example_str, top_n=5)
    
    # Check if the returned object is a matplotlib AxesSubplot
    assert isinstance(ax, plt.Axes)
    
    # Check if the top_n_words is a dictionary
    assert isinstance(top_n_words, dict)
    
    # Check if the dictionary is empty
    assert len(top_n_words) == 0