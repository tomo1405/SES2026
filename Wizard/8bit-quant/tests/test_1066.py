python
import pytest
import numpy as np
from scipy import fftpack
from matplotlib import pyplot as plt

def task_func(arr):
    row_sums = arr.sum(axis=1)
    fft_coefficients = fftpack.fft(row_sums)

    _, ax = plt.subplots()
    ax.plot(np.abs(fft_coefficients))
    ax.set_title("Absolute values of FFT coefficients")

    return ax

def test_task_func():
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    ax = task_func(arr)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Absolute values of FFT coefficients"
    assert ax.get_xlabel() == "Frequency"
    assert ax.get_ylabel() == "Magnitude"
    assert ax.get_xlim() == (0, 1)
    assert ax.get_ylim() == (0, 1)
    assert ax.get_xticks() == [0, 1]
    assert ax.get_yticks() == [0, 1]
    assert ax.get_xticklabels() == ['0', '1']
    assert ax.get_yticklabels() == ['0', '1']
    assert ax.get_lines()[0].get_data() == (np.arange(2), [0, 1])
    assert ax.get_lines()[0].get_color() == 'black'
    assert ax.get_lines()[0].get_linestyle() == '-'
    assert ax.get_lines()[0].get_linewidth() == 1.0
    assert ax.get_lines()[0].get_marker() == 'None'
    assert ax.get_lines()[0].get_markersize() == 1.0
    assert ax.get_lines()[0].get_markeredgewidth() == 1.0
    assert ax.get_lines()[0].get_markerfacecolor() == 'None'
    assert ax.get_lines()[0].get_label() == 'Magnitude'
    assert ax.get_legend().get_texts()[0].get_text() == 'Magnitude'
    assert ax.get_legend().get_texts()[0].get_color() == 'black'
    assert ax.get_legend().get_texts()[0].get_fontsize() == 'medium'
    assert ax.get_legend().get_texts()[0].get_fontweight() == 'normal'
    assert ax.get_legend().get_lines()[0].get_data() == ([0], [0])
    assert ax.get_legend().get_lines()[0].get_color() == 'black'
    assert ax.get_legend().get_lines()[0].get_linestyle() == '-'
    assert ax.get_legend().get_lines()[0].get_linewidth() == 1.0
    assert ax.get_legend().get_lines()[0].get_marker() == 'None'
    assert ax.get_legend().get_lines()[0].get_markersize() == 1.0
    assert ax.get_legend().get_lines()[0].get_markeredgewidth() == 1.0
    assert ax.get_legend().get_lines()[0].get_markerfacecolor() == 'None'
    assert ax.get_legend().get_lines()[0].get_label() == 'Magnitude'