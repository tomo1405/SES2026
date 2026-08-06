import pandas as pd
import numpy as np
from random import choice, seed as set_seed
from src_0118 import task_func
import pytest

def test_task_func():
    num_of_students = 10
    seed = 42
    name_list = ['John', 'Mike', 'Sara', 'Emma', 'Nick']
    gender_list = ['Male', 'Female']
    age_range = (15, 20)
    score_range = (50, 100)
    df = task_func(num_of_students, seed, name_list, gender_list, age_range, score_range)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (num_of_students, 4)
    assert df.columns.tolist() == ['Name', 'Age', 'Gender', 'Score']
    for _, row in df.iterrows():
        assert row['Name'] in name_list
        assert row['Age'] >= age_range[0] and row['Age'] <= age_range[1]
        assert row['Gender'] in gender_list
        assert row['Score'] >= score_range[0] and row['Score'] <= score_range[1]

def test_task_func_invalid_num_of_students():
    with pytest.raises(ValueError):
        task_func(0, 42, ['John', 'Mike', 'Sara', 'Emma', 'Nick'], ['Male', 'Female'], (15, 20), (50, 100))