import random

import pandas as pd
from src_0172 import task_func


def test_task_func():
    vegetable_dict = {'Carrot': 10, 'Potato': 20, 'Tomato': 30, 'Cabbage': 40, 'Spinach': 50}
    seed = 0
    expected_output = pd.DataFrame({
        'Count': [10, 20, 30, 40, 50],
        'Percentage': [20.0, 40.0, 60.0, 80.0, 100.0]
    }, index=VEGETABLES)
    random.seed(seed)
    actual_output = task_func(vegetable_dict, seed)
    assert actual_output.equals(expected_output)

def test_task_func_with_seed_1():
    vegetable_dict = {'Carrot': 10, 'Potato': 20, 'Tomato': 30, 'Cabbage': 40, 'Spinach': 50}
    seed = 1
    expected_output = pd.DataFrame({
        'Count': [5, 7, 10, 12, 15],
        'Percentage': [10.0, 14.0, 20.0, 24.0, 30.0]
    }, index=VEGETABLES)
    random.seed(seed)
    actual_output = task_func(vegetable_dict, seed)
    assert actual_output.equals(expected_output)

def test_task_func_with_seed_2():
    vegetable_dict = {'Carrot': 10, 'Potato': 20, 'Tomato': 30, 'Cabbage': 40, 'Spinach': 50}
    seed = 2
    expected_output = pd.DataFrame({
        'Count': [15, 12, 10, 7, 5],
        'Percentage': [30.0, 24.0, 20.0, 14.0, 10.0]
    }, index=VEGETABLES)
    random.seed(seed)
    actual_output = task_func(vegetable_dict, seed)
    assert actual_output.equals(expected_output)