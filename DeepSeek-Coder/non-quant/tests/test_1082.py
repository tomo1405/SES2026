import pytest
from src_1082 import task_func
import pandas as pd
import seaborn as sns

def test_task_func():
    # Test case 1: Default data
    result = task_func()
    assert isinstance(result, sns.axisgrid.Axes)

    # Add more test cases as needed