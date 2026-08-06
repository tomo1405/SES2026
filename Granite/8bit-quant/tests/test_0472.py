import pytest
from collections import Counter
import pandas as pd
from src_0472 import task_func

def test_task_func():
    myList = ["Hello", "World", "Hello", "World", "hello", "world"]
    expected_report_df = pd.DataFrame({"Count": [2, 2]}, index=["hello", "world"])
    report_df = task_func(myList)
    assert report_df.equals(expected_report_df)

def test_task_func_empty_list():
    myList = []
    expected_report_df = pd.DataFrame({"Count": []})
    report_df = task_func(myList)
    assert report_df.equals(expected_report_df)

def test_task_func_one_element_list():
    myList = ["Hello"]
    expected_report_df = pd.DataFrame({"Count": [1]}, index=["hello"])
    report_df = task_func(myList)
    assert report_df.equals(expected_report_df)

def test_task_func_with_numbers():
    myList = ["Hello", "1", "2", "3"]
    expected_report_df = pd.DataFrame({"Count": [1, 1, 1]}, index=["hello", "1", "2"])
    report_df = task_func(myList)
    assert report_df.equals(expected_report_df)