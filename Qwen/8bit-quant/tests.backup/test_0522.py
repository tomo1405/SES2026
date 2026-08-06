import pytest
from src_0522 import task_func
import pandas as pd
import io
import matplotlib.pyplot as plt

# Mocking plt.savefig to capture the plot output
def mock_savefig(fig, fname, format=None, **kwargs):
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    with open(fname, 'wb') as f:
        f.write(buf.read())

@pytest.fixture
def data_list():
    return [
        {'Test 1': 85, 'Test 2': 90, 'Test 3': 78},
        {'Test 1': 88, 'Test 2': 92, 'Test 3': 80},
        {'Test 1': 90, 'Test 2': 85, 'Test 3': 79}
    ]

def test_task_func(data_list, monkeypatch):
    # Monkeypatch plt.savefig to use our mock_savefig function
    monkeypatch.setattr(plt, 'savefig', mock_savefig)

    # Call the function
    ax = task_func(data_list)

    # Check if the axis object is created correctly
    assert isinstance(ax, plt.Axes)

    # Check if the title and labels are set correctly
    assert ax.get_title() == "Student Scores over Tests"
    assert ax.get_xlabel() == "Test Number"
    assert ax.get_ylabel() == "Score"

    # Check if the correct number of lines are plotted
    assert len(ax.lines) == len(data_list[0])

    # Check if the lines have the correct labels
    line_labels = [line.get_label() for line in ax.lines]
    assert sorted(line_labels) == sorted(data_list[0].keys())

    # Save the plot to a file and check if it exists
    output_file = 'test_plot.png'
    plt.savefig(output_file)
    assert open(output_file, 'rb').read() != b''