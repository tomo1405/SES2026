import pandas as pd
from random import randint, seed as random_seed
import statistics
import numpy as np
from src_0127 import task_func
import pytest

@pytest.fixture
def setup():
    random_seed(42)
    animals = ['Lion', 'Elephant', 'Tiger', 'Giraffe', 'Panda']
    report_data = []

    for animal in animals:
        counts = [randint(1, 100) for _ in range(10)]
        mean = statistics.mean(counts)
        median = statistics.median(counts)
        mode = statistics.mode(counts)
        std_dev = np.std(counts)
        report_data.append([animal, mean, median, mode, std_dev])
    
    report_df = pd.DataFrame(report_data, columns=['Animal', 'Mean', 'Median', 'Mode', 'Standard Deviation'])

    return report_df

def test_task_func_default_args(setup):
    report_df = task_func()
    assert isinstance(report_df, pd.DataFrame)
    assert report_df.shape == (5, 5)
    assert report_df.columns.tolist() == ['Animal', 'Mean', 'Median', 'Mode', 'Standard Deviation']

def test_task_func_custom_args(setup):
    animals = ['Lion', 'Elephant', 'Tiger', 'Giraffe']
    report_df = task_func(animals=animals)
    assert isinstance(report_df, pd.DataFrame)
    assert report_df.shape == (4, 5)
    assert report_df.columns.tolist() == ['Animal', 'Mean', 'Median', 'Mode', 'Standard Deviation']

def test_task_func_invalid_arg_type():
    with pytest.raises(TypeError):
        task_func(animals='Lion')

def test_task_func_invalid_arg_value():
    with pytest.raises(ValueError):
        task_func(animals=['Lion', 'Elephant', 'Tiger', 'Giraffe', 'Panda', 'Lion'])