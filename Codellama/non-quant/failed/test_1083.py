import pytest
from src_1083 import task_func
import pandas as pd
from scipy.stats import pearsonr

def test_task_func():
    data = [
        {"Score_String": "100", "Grade": "A"},
        {"Score_String": "90", "Grade": "B"},
        {"Score_String": "80", "Grade": "C"},
        {"Score_String": "70", "Grade": "D"},
        {"Score_String": "60", "Grade": "F"}
    ]
    df = pd.DataFrame(data)
    expected_correlation = pearsonr(df["Score_Float"], df["Grade_Encoded"])[0]
    assert task_func(data) == expected_correlation

def test_task_func_with_invalid_data():
    data = [
        {"Score_String": "100", "Grade": "A"},
        {"Score_String": "90", "Grade": "B"},
        {"Score_String": "80", "Grade": "C"},
        {"Score_String": "70", "Grade": "D"},
        {"Score_String": "60", "Grade": "F"}
    ]
    df = pd.DataFrame(data)
    df["Score_String"] = df["Score_String"].astype(float)
    df["Grade"] = df["Grade"].astype("category").cat.codes
    expected_correlation = pearsonr(df["Score_Float"], df["Grade_Encoded"])[0]
    assert task_func(data) == expected_correlation

def test_task_func_with_empty_data():
    data = []
    df = pd.DataFrame(data)
    expected_correlation = float("nan")
    assert task_func(data) == expected_correlation

def test_task_func_with_invalid_data_type():
    data = [
        {"Score_String": "100", "Grade": "A"},
        {"Score_String": "90", "Grade": "B"},
        {"Score_String": "80", "Grade": "C"},
        {"Score_String": "70", "Grade": "D"},
        {"Score_String": "60", "Grade": "F"}
    ]
    df = pd.DataFrame(data)
    df["Score_String"] = df["Score_String"].astype(int)
    df["Grade"] = df["Grade"].astype("category").cat.codes
    expected_correlation = float("nan")
    assert task_func(data) == expected_correlation