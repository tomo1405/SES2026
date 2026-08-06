import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pytest

from src_1037 import task_func

def test_task_func():
    s1 = pd.Series([1, 2, 3, 4, 5])
    s2 = pd.Series([4, 5, 6, 7, 8])
    ax, intersection_length = task_func(s1, s2)
    assert ax is not None
    assert intersection_length == 2