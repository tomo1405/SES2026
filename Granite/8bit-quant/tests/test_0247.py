import numpy as np
import pytest
from src_0247 import task_func


@pytest.mark.parametrize("n_waves, seed, expected_output", [
    (0, 0, ([], np.array([]), None)),
    (1, 0, ([np.sin(ANGLES)], fft(np.sin(ANGLES)), ax)),
    (2, 0, ([np.sin(ANGLES), np.sin(2*ANGLES)], fft(np.sin(ANGLES) + np.sin(2*ANGLES)), ax)),
    (3, 1, ([np.sin(ANGLES), np.sin(2*ANGLES), np.sin(3*ANGLES)], fft(np.sin(ANGLES) + np.sin(2*ANGLES) + np.sin(3*ANGLES)), ax)),
])
def test_task_func(n_waves, seed, expected_output):
    sine_wave_series, fft_data, ax = task_func(n_waves, seed)
    assert (sine_wave_series, fft_data, ax) == expected_output