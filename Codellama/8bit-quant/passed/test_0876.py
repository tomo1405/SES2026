import pytest
from src_0876 import task_func
import pandas as pd
import random

def test_task_func_with_seed():
    data = [['Alice', 25, 'Engineer'], ['Bob', 30, 'Doctor'], ['Charlie', 35, 'Teacher']]
    columns = ['Name', 'Age', 'Occupation']
    fill_missing = True
    num_range = (0, 100)
    seed = 1234

    expected_output = pd.DataFrame([['Alice', 25, 'Engineer'], ['Bob', 30, 'Doctor'], ['Charlie', 35, 'Teacher']], columns=columns)
    expected_output['Age'] = expected_output['Age'].apply(lambda x: random.randint(*num_range) if pd.isnull(x) else x)

    random.seed(seed)
    output = task_func(data, columns, fill_missing, num_range, seed)

    assert output.equals(expected_output)

def test_task_func_without_seed():
    data = [['Alice', 25, 'Engineer'], ['Bob', 30, 'Doctor'], ['Charlie', 35, 'Teacher']]
    columns = ['Name', 'Age', 'Occupation']
    fill_missing = True
    num_range = (0, 100)

    expected_output = pd.DataFrame([['Alice', 25, 'Engineer'], ['Bob', 30, 'Doctor'], ['Charlie', 35, 'Teacher']], columns=columns)
    expected_output['Age'] = expected_output['Age'].apply(lambda x: random.randint(*num_range) if pd.isnull(x) else x)

    output = task_func(data, columns, fill_missing, num_range)

    assert output.equals(expected_output)