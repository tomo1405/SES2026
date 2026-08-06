import pandas as pd
from random import shuffle, randint
from src_0577 import task_func

def test_task_func():
    l = ["abc", "def", "ghi", "jkl"]
    expected_output = pd.Series(["bcj", "efk", "igh", "ljk"])
    output = task_func(l)
    assert output.equals(expected_output)

def test_task_func_with_empty_list():
    l = []
    expected_output = pd.Series()
    output = task_func(l)
    assert output.equals(expected_output)

def test_task_func_with_one_element_list():
    l = ["a"]
    expected_output = pd.Series(["a"])
    output = task_func(l)
    assert output.equals(expected_output)

def test_task_func_with_n_groups_equal_to_zero():
    l = ["abc", "def", "ghi", "jkl"]
    expected_output = pd.Series(["abc", "def", "ghi", "jkl"])
    output = task_func(l, n_groups=0)
    assert output.equals(expected_output)

def test_task_func_with_n_groups_greater_than_length_of_list():
    l = ["abc", "def", "ghi", "jkl"]
    expected_output = pd.Series(["abc", "def", "ghi", "jkl"])
    output = task_func(l, n_groups=len(l) + 1)
    assert output.equals(expected_output)