import random

import pandas as pd
from src_0172 import task_func


def test_task_func():
    vegetable_dict = {'Carrot': 5, 'Potato': 3, 'Tomato': 7, 'Cabbage': 2, 'Spinach': 4}
    seed = 0
    expected_output = pd.DataFrame({
        'Count': [5, 3, 7, 2, 4],
        'Percentage': [15.0, 7.5, 22.5, 5.0, 10.0]
    }, index=VEGETABLES)
    random.seed(seed)
    actual_output = task_func(vegetable_dict, seed)
    assert actual_output.equals(expected_output)

def test_task_func_with_seed_none():
    vegetable_dict = {'Carrot': 5, 'Potato': 3, 'Tomato': 7, 'Cabbage': 2, 'Spinach': 4}
    seed = None
    expected_output = pd.DataFrame({
        'Count': [5, 3, 7, 2, 4],
        'Percentage': [15.0, 7.5, 22.5, 5.0, 10.0]
    }, index=VEGETABLES)
    random.seed(seed)
    actual_output = task_func(vegetable_dict, seed)
    assert actual_output.equals(expected_output)

def test_task_func_with_seed_123():
    vegetable_dict = {'Carrot': 5, 'Potato': 3, 'Tomato': 7, 'Cabbage': 2, 'Spinach': 4}
    seed = 123
    expected_output = pd.DataFrame({
        'Count': [5, 3, 7, 2, 4],
        'Percentage': [15.0, 7.5, 22.5, 5.0, 10.0]
    }, index=VEGETABLES)
    random.seed(seed)
    actual_output = task_func(vegetable_dict, seed)
    assert actual_output.equals(expected_output)