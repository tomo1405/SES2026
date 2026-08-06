import pandas as pd
import re
from scipy import stats
from src_0322 import task_func
import pytest

def test_task_func():
    # Test case 1: No names found in the text
    text1 = "This is a sample text without any names."
    name_freqs1, ax1, skewness1, kurtosis1 = task_func(text1)
    assert name_freqs1.empty
    assert ax1 is None
    assert skewness1 is None
    assert kurtosis1 is None

    # Test case 2: Names found in the text
    text2 = "John and Jane are in the room. Sarah[tag] is also there."
    name_freqs2, ax2, skewness2, kurtosis2 = task_func(text2)
    assert name_freqs2.tolist() == ['John', 'Jane', 'Sarah']
    assert ax2 is not None
    assert skewness2 is not None
    assert kurtosis2 is not None