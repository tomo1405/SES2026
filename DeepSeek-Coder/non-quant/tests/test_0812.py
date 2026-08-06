import pytest
from src_0812 import task_func
import pandas as pd
from random import randint, seed

# Test cases for task_func

def test_task_func_basic():
    dictionary = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    item = 2
    result = task_func(dictionary, item)
    assert isinstance(result, tuple), "The result should be a tuple"
    assert len(result) == 2, "The result should contain two elements"
    assert isinstance(result[0], list), "The first element should be a list"
    assert isinstance(result[1], pd.DataFrame), "The second element should be a DataFrame"

def test_task_func_with_sample():
    dictionary = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    item = 2
    sample_size = 1
    result = task_func(dictionary, item, sample_size=sample_size)
    assert isinstance(result, tuple), "The result should be a tuple"
    assert len(result) == 2, "The result should contain two elements"
    assert isinstance(result[0], list), "The first element should be a list"
    assert isinstance(result[1], pd.DataFrame), "The second element should be a DataFrame"
    assert len(result[0]) <= sample_size, "The sample size should be less than or equal to the sample size"

def test_task_func_with_seed():
    dictionary = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    item = 2
    random_seed = 42
    result = task_func(dictionary, item, random_seed=random_seed)
    assert isinstance(result, tuple), "The result should be a tuple"
    assert len(result) == 2, "The result should contain two elements"
    assert isinstance(result[0], list), "The first element should be a list"
    assert isinstance(result[1], pd.DataFrame), "The second element should be a DataFrame"