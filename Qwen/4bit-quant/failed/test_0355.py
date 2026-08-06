import pytest
from src_0355 import task_func
import collections
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func():
    # Test data
    sentences_dict = {
        'sentence1': 'The quick brown fox jumps over the lazy dog.',
        'sentence2': 'To be or not to be, that is the question.'
    }
    word_keys = ['the', 'be', 'to']

    # Expected output
    expected_word_counts = collections.Counter(' '.join(sentences_dict.values()).split())
    expected_frequencies = [expected_word_counts[word] for word in word_keys]
    expected_word_series = pd.Series(expected_frequencies, index=word_keys)

    # Actual output
    actual_word_series = task_func(sentences_dict, word_keys)

    # Check if the returned Series is as expected
    assert actual_word_series.equals(expected_word_series), "The returned Series does not match the expected output."

    # Check if the plot is created
    fig = plt.gcf()
    assert len(fig.axes) == 1, "No plot was created."
    assert fig.axes[0].get_title() == '', "The plot should not have a title by default."

    # Close the plot to avoid issues in subsequent tests
    plt.close(fig)