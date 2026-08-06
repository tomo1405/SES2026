import pytest
from src_0011 import task_func
import numpy as np
import itertools
import random
import statistics

def test_task_func():
    T1 = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    mean, median, mode = task_func(T1)
    assert isinstance(mean, float)
    assert isinstance(median, float)
    assert isinstance(mode, float)
    T1 = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], ["10", "11", "12"]]
    mean, median, mode = task_func(T1)
    assert mean > median > mode
    T1 = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], ["10", "11", "12"], ["13", "14", "15"]]
    mean, median, mode = task_func(T1)
    assert mean > median > mode
    T1 = []
    with pytest.raises(statistics.StatisticsError):
        mean, median, mode = task_func(T1)