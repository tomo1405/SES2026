import pytest
from src_0356 import task_func
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    amplitude = 1.0
    frequency = 5.0
    time = np.linspace(0, 1, 100)
    return amplitude, frequency, time

def test_task_func_output_type(sample_data):
    amplitude, frequency, time = sample_data
    wave, fig, ax = task_func(amplitude, frequency, time)
    assert isinstance(wave, np.ndarray)
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)

def test_task_func_wave_shape(sample_data):
    amplitude, frequency, time = sample_data
    wave, _, _ = task_func(amplitude, frequency, time)
    assert wave.shape == time.shape

def test_task_func_wave_values(sample_data):
    amplitude, frequency, time = sample_data
    wave, _, _ = task_func(amplitude, frequency, time)
    expected_wave = amplitude * np.exp(1j * 2 * np.pi * frequency * time)
    window = np.hanning(time.size)
    expected_wave *= window
    np.testing.assert_allclose(wave, expected_wave)

def test_task_func_plot_labels(sample_data):
    amplitude, frequency, time = sample_data
    _, fig, ax = task_func(amplitude, frequency, time)
    assert ax.get_title() == "Complex Wave with Hann Window"
    assert ax.get_xlabel() == "Time"
    assert ax.get_ylabel() == "Amplitude"
    legend_labels = [text.get_text() for text in ax.get_legend().get_texts()]
    assert set(legend_labels) == {"Real Part", "Imaginary Part"}

def test_task_func_plot_lines(sample_data):
    amplitude, frequency, time = sample_data
    _, fig, ax = task_func(amplitude, frequency, time)
    lines = ax.get_lines()
    assert len(lines) == 2
    assert lines[0].get_label() == "Real Part"
    assert lines[1].get_label() == "Imaginary Part"