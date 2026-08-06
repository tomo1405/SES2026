python
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.signal import get_window

def task_func(amplitude, frequency, time):
    wave = amplitude * np.exp(1j * 2 * math.pi * frequency * time)
    window = get_window('hann', time.size)  # Apply a Hann window
    wave *= window  # Apply the window to the wave

    # Plot the wave
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(time, np.real(wave), label="Real Part")
    ax.plot(time, np.imag(wave), label="Imaginary Part")
    ax.set_title("Complex Wave with Hann Window")
    ax.set_xlabel("Time")
    ax.set_ylabel("Amplitude")
    ax.legend()

    return wave, fig, ax

# Test the function with some inputs
wave, fig, ax = task_func(amplitude=1, frequency=1, time=np.arange(0, 1, 0.01))

# Check the output
assert isinstance(wave, np.ndarray), "Output is not a numpy array"
assert isinstance(fig, plt.Figure), "Output is not a matplotlib figure"
assert isinstance(ax, plt.Axes), "Output is not a matplotlib axes"