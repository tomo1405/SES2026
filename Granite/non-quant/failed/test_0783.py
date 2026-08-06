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

def test_task_func_output_type(input_args):
    output = task_func(**input_args)
    assert isinstance(output, pd.DataFrame)

def test_task_func_output_shape(input_args):
    output = task_func(**input_args)
    assert output.shape == (input_args["n"], 5)

def test_task_func_output_values(input_args):
    output = task_func(**input_args)
    assert output["title"].iloc[0] == "Article 0"
    assert output["title_url"].iloc[0] == "samplewebsite.com/Article_0"
    assert output["id"].iloc[0] == 0
    assert output["category"].iloc[0] in input_args["categories"]
    assert output["views"].iloc[0] > 0

def test_task_func_seed_consistency(input_args):
    output_1 = task_func(**input_args)
    input_args["random_seed"] = 42
    output_2 = task_func(**input_args)
    assert output_1.equals(output_2)

def test_task_func_invalid_input(input_args):
    with pytest.raises(ValueError):
        task_func(n=-1, **input_args)