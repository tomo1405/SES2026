import pytest
from src_0472 import task_func

def test_task_func():
    myList = ["hello", "world", "hello", "world", "hello"]
    expected_output = pd.DataFrame({"Count": [3, 2]}, index=["hello", "world"])
    assert task_func(myList).equals(expected_output)

def test_task_func_empty_input():
    myList = []
    expected_output = pd.DataFrame(columns=["Count"])
    assert task_func(myList).equals(expected_output)

def test_task_func_single_word():
    myList = ["hello"]
    expected_output = pd.DataFrame({"Count": [1]}, index=["hello"])
    assert task_func(myList).equals(expected_output)

def test_task_func_duplicate_words():
    myList = ["hello", "hello", "hello"]
    expected_output = pd.DataFrame({"Count": [3]}, index=["hello"])
    assert task_func(myList).equals(expected_output)