import math
import statistics
import numpy as np
from src_0220 import task_func

def test_task_func():
    input_list = [1, 2, 3, 4, 5]
    mean, median, mode, mean_fft, median_fft, mode_fft = task_func(input_list)
    assert isinstance(mean, float)
    assert isinstance(median, float)
    assert isinstance(mode, float)
    assert isinstance(mean_fft, int)
    assert isinstance(median_fft, int)
    assert isinstance(mode_fft, int)
    assert mean == statistics.mean(input_list)
    assert median == statistics.median(input_list)
    assert mode == statistics.mode(input_list)
    fft = np.abs(np.fft.fft([math.degrees(x) for x in input_list]))
    assert mean_fft == round(statistics.mean(fft))
    assert median_fft == round(statistics.median(fft))
    assert mode_fft == round(statistics.mode(fft))