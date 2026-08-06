python
import collections
from operator import itemgetter
import matplotlib.pyplot as plt
import pytest

def task_func(data):
    letter_counts = collections.Counter([item[0] for item in data])
    max_value_letter = max(data, key=itemgetter(1))[0]

    letters, counts = zip(*letter_counts.items())
    # Initialize a fresh plot
    plt.figure()
    ax = plt.bar(letters, counts, label='Letter Counts')

    if max_value_letter in letter_counts:
        plt.bar(max_value_letter, letter_counts[max_value_letter], color='red', label='Max Value Letter')

    plt.xlabel('Letter')
    plt.ylabel('Count')
    plt.title('Letter Counts with Max Value Letter Highlighted')
    plt.legend()

    return plt.gca()

def test_task_func():
    data = [('a', 10), ('b', 20), ('c', 30), ('d', 20), ('e', 10)]
    ax = task_func(data)
    assert ax.get_xlabel() == 'Letter'
    assert ax.get_ylabel() == 'Count'
    assert ax.get_title() == 'Letter Counts with Max Value Letter Highlighted'
    assert ax.get_legend_handles_labels()[1] == [('Letter Counts', 'Max Value Letter')]
    assert ax.patches[0].get_facecolor() == (0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 1.0)
    assert ax.patches[1].get_facecolor() == (1.0, 0.0, 0.0, 1.0)
    assert ax.patches[1].get_label() == 'Max Value Letter'