import pandas as pd
from random import randint, seed as random_seed
import statistics
import numpy as np
from src_0127 import task_func
import pytest

@pytest.fixture
def animals():
    return ['Lion', 'Elephant', 'Tiger', 'Giraffe', 'Panda']

@pytest.fixture
def seed():
    return 42

@pytest.fixture
def report_data(animals, seed):
    random_seed(seed)
    report_data = []

    for animal in animals:
        counts = [randint(1, 100) for _ in range(10)]
        mean = statistics.mean(counts)
        median = statistics.median(counts)
        mode = statistics.mode(counts)
        std_dev = np.std(counts)
        report_data.append([animal, mean, median, mode, std_dev])
    
    return report_data

@pytest.fixture
def report_df(report_data):
    return pd.DataFrame(report_data, columns=['Animal', 'Mean', 'Median', 'Mode', 'Standard Deviation'])

def test_task_func(animals, seed, report_data, report_df):
    result = task_func(animals=animals, seed=seed)
    assert result.equals(report_df)

def test_task_func_default_args(report_df):
    result = task_func()
    assert result.equals(report_df)