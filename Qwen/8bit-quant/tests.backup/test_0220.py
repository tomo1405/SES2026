import pytest
from src_0220 import task_func
import math
import statistics
import numpy as np

def test_task_func_with_empty_list():
    result = task_func([])
    assert result == (0.0, 0.0, 0.0, 0, 0, 0)

def test_task_func_with_single_element():
    result = task_func([1.0])
    assert result == (1.0, 1.0, 1.0, 1, 1, 1)

def test_task_func_with_multiple_elements():
    result = task_func([1.0, 2.0, 3.0])
    assert result == (2.0, 2.0, 1.0, 1, 1, 1)

def test_task_func_with_repeated_elements():
    result = task_func([1.0, 1.0, 2.0, 2.0, 3.0])
    assert result == (1.8, 2.0, 1.0, 1, 1, 1)

def test_task_func_with_negative_values():
    result = task_func([-1.0, -2.0, -3.0])
    assert result == (-2.0, -2.0, -3.0, 1, 1, 1)

def test_task_func_with_mixed_values():
    result = task_func([-1.0, 0.0, 1.0])
    assert result == (0.0, 0.0, 0.0, 1, 1, 1)

def test_task_func_with_large_numbers():
    result = task_func([100.0, 200.0, 300.0])
    assert result == (200.0, 200.0, 100.0, 1, 1, 1)

def test_task_func_with_small_numbers():
    result = task_func([0.001, 0.002, 0.003])
    assert result == (0.002, 0.002, 0.001, 1, 1, 1)

def test_task_func_with_pi_values():
    result = task_func([math.pi/4, math.pi/2, 3*math.pi/4])
    assert result == (math.pi/2, math.pi/2, math.pi/4, 1, 1, 1)

def test_task_func_with_random_values():
    np.random.seed(0)
    random_values = np.random.rand(10)
    result = task_func(random_values)
    expected_mean = statistics.mean(random_values)
    expected_median = statistics.median(random_values)
    expected_mode = statistics.mode(random_values)
    fft = np.abs(np.fft.fft([math.degrees(x) for x in random_values]))
    expected_mean_fft = round(statistics.mean(fft))
    expected_median_fft = round(statistics.median(fft))
    expected_mode_fft = round(statistics.mode(fft))
    assert result == (expected_mean, expected_median, expected_mode, expected_mean_fft, expected_median_fft, expected_mode_fft)