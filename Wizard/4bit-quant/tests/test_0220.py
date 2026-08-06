python
import math
import statistics
import numpy as np
import pytest

def task_func(input_list):
    fft = np.abs(np.fft.fft([math.degrees(x) for x in input_list]))
    sorted_list = sorted(input_list, key=lambda x: (math.degrees(x), x))
    mean = statistics.mean(sorted_list)
    median = statistics.median(sorted_list)
    mode = statistics.mode(sorted_list)
    mean_fft = round(statistics.mean(fft))
    median_fft = round(statistics.median(fft))
    mode_fft = round(statistics.mode(fft))
    return (mean, median, mode, mean_fft, median_fft, mode_fft)

def test_task_func():
    input_list = [10, 20, 30, 40, 50]
    expected_output = (20, 30, 30, 20, 30, 20)
    assert task_func(input_list) == expected_output