import pytest
import random
import pandas as pd
import numpy as np
from src_0783 import task_func

@pytest.fixture
def input_args():
    return {
        "n": 10,
        "domain": "samplewebsite.com",
        "categories": ['Sports', 'Technology', 'Health', 'Science', 'Business'],
        "random_seed": None
    }

def test_task_func(input_args):
    df = task_func(**input_args)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == input_args["n"]
    assert all(col in df.columns for col in ["title", "title_url", "id", "category", "views"])

def test_task_func_seed(input_args):
    input_args_copy = input_args.copy()
    df1 = task_func(**input_args)
    input_args_copy["random_seed"] = 42
    df2 = task_func(**input_args_copy)
    assert df1.equals(df2)

def test_task_func_invalid_input(input_args):
    with pytest.raises(ValueError):
        task_func(n=-1, **input_args)