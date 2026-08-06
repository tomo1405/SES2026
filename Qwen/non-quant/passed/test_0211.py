import pytest
from src_0211 import task_func
import collections
from operator import itemgetter
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    return [('a', 10), ('b', 20), ('c', 15), ('a', 25)]

def test_task_func(sample_data):
    fig = task_func(sample_data)
    assert isinstance(fig, plt.Axes)

    # Check if the bar chart is plotted correctly
    bars = fig.patches
    expected_letters = ['a', 'b', 'c']
    expected_counts = [2, 20, 15]

    for i, bar in enumerate(bars):
        assert bar.get_height() == expected_counts[i]
        assert bar.get_x() == i * 0.8  # Assuming default bar width and spacing

    # Check if the max value letter is highlighted
    max_value_letter = max(sample_data, key=itemgetter(1))[0]
    max_bar = next(bar for bar in bars if bar.get_x() == expected_letters.index(max_value_letter) * 0.8)
    assert max_bar.get_color() == 'red'

    # Check if labels and title are set correctly
    assert fig.get_xlabel() == 'Letter'
    assert fig.get_ylabel() == 'Count'
    assert fig.get_title() == 'Letter Counts with Max Value Letter Highlighted'

    # Check if legend is present
    legend = fig.get_legend()
    assert legend is not None
    assert len(legend.get_texts()) == 2
    assert legend.get_texts()[0].get_text() == 'Letter Counts'
    assert legend.get_texts()[1].get_text() == 'Max Value Letter'