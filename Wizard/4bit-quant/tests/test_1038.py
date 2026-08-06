python
import pandas as pd
import pytest
from src_1038 import task_func

def test_task_func():
    s1 = pd.Series([1, 2, 3, 4, 5])
    s2 = pd.Series([2, 4, 6, 8, 10])
    labels, ax = task_func(s1, s2)
    assert len(labels) == 5
    assert ax.get_xlabel() == s1.name
    assert ax.get_ylabel() == s2.name
    assert ax.get_title() == "K-Means Clustering"