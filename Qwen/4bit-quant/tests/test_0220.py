import math
import statistics

import numpy as np
from src_0220 import task_func


def test_task_func_with_empty_list():
    assert task_func([]) == (0, 0, 0, 0, 0, 0)

def test_task_func_with_single_element():
    assert task_func([0]) == (0, 0, 0, 0, 0, 0)

def test_task_func_with_two_elements():
    assert task_func([0, math.pi/2]) == (0.7853981633974483, 0.7853981633974483, 0.7853981633974483, 0, 0, 0)

def test_task_func_with_multiple_elements():
    input_list = [0, math.pi/4, math.pi/2, math.pi]
    result = task_func(input_list)
    expected_mean = statistics.mean([0, 45, 90, 180])
    expected_median = statistics.median([0, 45, 90, 180])
    expected_mode = statistics.mode([0, 45, 90, 180])
    fft = np.abs(np.fft.fft([math.degrees(x) for x in input_list]))
    expected_mean_fft = round(statistics.mean(fft))
    expected_median_fft = round(statistics.median(fft))
    expected_mode_fft = round(statistics.mode(fft))
    assert result == (expected_mean, expected_median, expected_mode, expected_mean_fft, expected_median_fft, expected_mode_fft)

def test_task_func_with_repeated_elements():
    input_list = [math.pi/4, math.pi/4, math.pi/2, math.pi/2]
    result = task_func(input_list)
    expected_mean = statistics.mean([45, 45, 90, 90])
    expected_median = statistics.median([45, 45, 90, 90])
    expected_mode = statistics.mode([45, 45, 90, 90])
    fft = np.abs(np.fft.fft([math.degrees(x) for x in input_list]))
    expected_mean_fft = round(statistics.mean(fft))
    expected_median_fft = round(statistics.median(fft))
    expected_mode_fft = round(statistics.mode(fft))
    assert result == (expected_mean, expected_median, expected_mode, expected_mean_fft, expected_median_fft, expected_mode_fft)

def test_task_func_with_negative_angles():
    input_list = [-math.pi/2, -math.pi/4, 0, math.pi/4]
    result = task_func(input_list)
    expected_mean = statistics.mean([-90, -45, 0, 45])
    expected_median = statistics.median([-90, -45, 0, 45])
    expected_mode = statistics.mode([-90, -45, 0, 45])
    fft = np.abs(np.fft.fft([math.degrees(x) for x in input_list]))
    expected_mean_fft = round(statistics.mean(fft))
    expected_median_fft = round(statistics.median(fft))
    expected_mode_fft = round(statistics.mode(fft))
    assert result == (expected_mean, expected_median, expected_mode, expected_mean_fft, expected_median_fft, expected_mode_fft)