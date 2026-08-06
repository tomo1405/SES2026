import pandas as pd
from scipy.stats import pearsonr
from src_1083 import task_func
import pytest

def test_task_func():
    data = [["A", 85, "B"], ["B", 90, "A"], ["C", 75, "C"]]
    df = pd.DataFrame(data, columns=["Grade", "Score_String", "Letter_Grade"])
    correlation = task_func(data)
    assert correlation == pearsonr(df["Score_String"].astype(float), df["Letter_Grade"].astype("category").cat.codes)[0]

def test_task_func_with_nan():
    data = [["A", 85, "B"], ["B", float("nan"), "A"], ["C", 75, "C"]]
    df = pd.DataFrame(data, columns=["Grade", "Score_String", "Letter_Grade"])
    correlation = task_func(data)
    assert correlation == pearsonr(df["Score_String"].astype(float), df["Letter_Grade"].astype("category").cat.codes)[0]

def test_task_func_with_less_than_two_rows():
    data = [["A", 85, "B"]]
    df = pd.DataFrame(data, columns=["Grade", "Score_String", "Letter_Grade"])
    correlation = task_func(data)
    assert correlation == float("nan")