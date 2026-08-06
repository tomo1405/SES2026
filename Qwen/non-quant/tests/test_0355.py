import pytest
from src_0355 import task_func
import collections
import pandas as pd
import matplotlib.pyplot as plt

# Mocking matplotlib to avoid actual plotting
class MockPlot:
    def plot(self, kind='bar'):
        pass

plt.bar = MockPlot().plot

def test_task_func():
    sentences_dict = {
        'sentence1': 'The quick brown fox jumps over the lazy dog',
        'sentence2': 'To be or not to be, that is the question',
        'sentence3': 'In a hole in the ground there lived a hobbit'
    }
    word_keys = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I']

    result = task_func(sentences_dict, word_keys)

    # Check if the result is a matplotlib Axes object
    assert isinstance(result, plt.Axes)

    # Check if the word_series is created correctly
    expected_counts = [4, 2, 2, 0, 0, 1, 2, 1, 0, 0]
    word_counts = collections.Counter(' '.join(sentences_dict.values()).split())
    frequencies = [word_counts[word] for word in word_keys]
    word_series = pd.Series(frequencies, index=word_keys)

    assert word_series.tolist() == expected_counts