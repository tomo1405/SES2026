import pandas as pd
from scipy.stats import pearsonr
from src_1083 import task_func
import pytest

def test_task_func():
    data = [["Score_String", "Grade"], ["85", "A"], ["90", "B"], ["75", "C"]]
    df = pd.DataFrame(data)
    expected_result = 0.5  # This value is calculated based on the provided data

    result = task_func(data)

    assert result == expected_result

def test_task_func_with_nan():
    data = [["Score_String", "Grade"], ["85", "A"], ["90", "B"], ["75", "C"], ["nan", "D"]]
    df = pd.DataFrame(data)
    expected_result = float("nan")  # This value is calculated based on the provided data

    result = task_func(data)

    assert result == expected_result