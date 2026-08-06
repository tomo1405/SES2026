python
import collections
import matplotlib.pyplot as plt
import pandas as pd

# Constants
WORDS = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I']

def task_func(sentences_dict, word_keys):
    word_counts = collections.Counter(' '.join(sentences_dict.values()).split())
    frequencies = [word_counts[word] for word in word_keys]
    word_series = pd.Series(frequencies, index=word_keys)
    plt.figure()
    word_series.plot(kind='bar')
    return word_series.plot(kind='bar')

# Test cases
def test_task_func():
    sentences_dict = {'sentence1': 'the quick brown fox jumps over the lazy dog',
                      'sentence2': 'the quick brown dog jumps over the lazy fox',
                      'sentence3': 'the quick brown fox jumps over the lazy dog',
                      'sentence4': 'the quick brown dog jumps over the lazy fox'}
    word_keys = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'lazy', 'dog']
    result = task_func(sentences_dict, word_keys)
    assert isinstance(result, plt.Axes)

test_task_func()