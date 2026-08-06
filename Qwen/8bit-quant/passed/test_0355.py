import pytest
from src_0355 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

# Mocking matplotlib to capture plot output
class MockPlot:
    def __init__(self):
        self.figures = []

    def savefig(self, *args, **kwargs):
        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        self.figures.append(base64.b64encode(buf.read()).decode('utf-8'))

@pytest.fixture
def mock_plot(monkeypatch):
    mock_plot_instance = MockPlot()
    monkeypatch.setattr(plt, 'savefig', mock_plot_instance.savefig)
    return mock_plot_instance

def test_task_func(mock_plot):
    sentences_dict = {
        'sentence1': 'The quick brown fox jumps over the lazy dog.',
        'sentence2': 'I have a dream that one day this nation will rise up and live out the true meaning of its creed.'
    }
    word_keys = ['the', 'I', 'dream']

    # Call the function
    ax = task_func(sentences_dict, word_keys)

    # Check if the plot was created
    assert len(mock_plot.figures) == 1

    # Check if the returned object is a matplotlib Axes
    assert isinstance(ax, plt.AxesSubplot)

    # Check if the Series is correctly created
    expected_series = pd.Series([2, 1, 1], index=word_keys)
    actual_series = ax.get_legend_handles_labels()[0][0].get_ydata()
    assert all(actual_series == expected_series)

    # Check if the plot has the correct labels
    assert ax.get_xlabel() == 'Word'
    assert ax.get_ylabel() == 'Frequency'
    assert ax.get_title() == ''