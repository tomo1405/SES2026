import pandas as pd
from scipy.stats import pearsonr
from src_1083 import task_func
import pytest

def test_task_func():
    data = [["Score_String", "Grade"], ["85", "A"], ["90", "B"], ["75", "C"]]
    df = pd.DataFrame(data)
    correlation = task_func(data)
    assert correlation == pearsonr(df["Score_String"].astype(float), df["Grade"].astype("category").cat.codes)[0]

def test_task_func_with_nan():
    data = [["Score_String", "Grade"], ["85", "A"], ["90", "B"], ["75", "C"], ["nan", "D"]]
    df = pd.DataFrame(data)
    correlation = task_func(data)
    assert correlation == pearsonr(df["Score_String"].astype(float), df["Grade"].astype("category").cat.codes)[0]

def test_task_func_with_less_than_two_rows():
    data = [["Score_String", "Grade"], ["85", "A"]]
    df = pd.DataFrame(data)
    correlation = task_func(data)
    assert correlation != pearsonr(df["Score_String"].astype(float), df["Grade"].astype("category").cat.codes)[0]