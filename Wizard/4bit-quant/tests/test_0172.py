python
import random
import pandas as pd
import collections

# Constants
VEGETABLES = ['Carrot', 'Potato', 'Tomato', 'Cabbage', 'Spinach']

def task_func(vegetable_dict, seed=0):
    random.seed(seed)
    # Create a counter for vegetables based on reversed dictionary
    reversed_dict = {v: k for k, v in vegetable_dict.items()}
    vegetable_counter = collections.Counter({vegetable: random.randint(1, 10) for vegetable in reversed_dict.keys()})

    statistics_df = pd.DataFrame.from_dict(vegetable_counter, orient='index', columns=['Count'])
    statistics_df['Percentage'] = statistics_df['Count'] / statistics_df['Count'].sum() * 100

    return statistics_df

def test_task_func():
    # Test case 1
    vegetable_dict = {'Carrot': 10, 'Potato': 20, 'Tomato': 30, 'Cabbage': 40, 'Spinach': 50}
    expected_result = pd.DataFrame({'Count': [10, 20, 30, 40, 50], 'Percentage': [10.0, 20.0, 30.0, 40.0, 50.0]}, index=VEGETABLES)
    assert task_func(vegetable_dict).equals(expected_result)

    # Test case 2
    vegetable_dict = {'Carrot': 10, 'Potato': 20, 'Tomato': 30, 'Cabbage': 40, 'Spinach': 50}
    expected_result = pd.DataFrame({'Count': [10, 20, 30, 40, 50], 'Percentage': [10.0, 20.0, 30.0, 40.0, 50.0]}, index=VEGETABLES)
    assert task_func(vegetable_dict, seed=1).equals(expected_result)

    # Test case 3
    vegetable_dict = {'Carrot': 10, 'Potato': 20, 'Tomato': 30, 'Cabbage': 40, 'Spinach': 50}
    expected_result = pd.DataFrame({'Count': [10, 20, 30, 40, 50], 'Percentage': [10.0, 20.0, 30.0, 40.0, 50.0]}, index=VEGETABLES)
    assert task_func(vegetable_dict, seed=2).equals(expected_result)

    # Test case 4
    vegetable_dict = {'Carrot': 10, 'Potato': 20, 'Tomato': 30, 'Cabbage': 40, 'Spinach': 50}
    expected_result = pd.DataFrame({'Count': [10, 20, 30, 40, 50], 'Percentage': [10.0, 20.0, 30.0, 40.0, 50.0]}, index=VEGETABLES)
    assert task_func(vegetable_dict, seed=3).equals(expected_result)

    # Test case 5
    vegetable_dict = {'Carrot': 10, 'Potato': 20, 'Tomato': 30, 'Cabbage': 40, 'Spinach': 50}
    expected_result = pd.DataFrame({'Count': [10, 20, 30, 40, 50], 'Percentage': [10.0, 20.0, 30.0, 40.0, 50.0]}, index=VEGETABLES)
    assert task_func(vegetable_dict, seed=4).equals(expected_result)

    # Test case 6
    vegetable_dict = {'Carrot': 10, 'Potato': 20, 'Tomato': 30, 'Cabbage': 40, 'Spinach': 50}
    expected_result = pd.DataFrame({'Count': [10, 20, 30, 40, 50], 'Percentage': [10.0, 20.0, 30.0, 40.0, 50.0]}, index=VEGETABLES)
    assert task_func(vegetable_dict, seed=5).equals(expected_result)

    # Test case 7
    vegetable_dict = {'Carrot': 10, 'Potato': 20, 'Tomato': 30, 'Cabbage': 40, 'Spinach': 50}
    expected_result = pd.DataFrame({'Count': [10, 20, 30, 40, 50], 'Percentage': [10.0, 20.0, 30.0, 40.0, 50.0]}, index=VEGETABLES)
    assert task_func(vegetable_dict, seed=6).equals(expected_result)

    # Test case 8
    vegetable_dict = {'Carrot': 10, 'Potato': 20, 'Tomato': 30, 'Cabbage': 40, 'Spinach': 50}
    expected_result = pd.DataFrame({'Count': [10, 20, 30, 40, 50], 'Percentage': [10.0, 20.0, 30.0, 40.0, 50.0]}, index=VEGETABLES)
    assert task_func(vegetable_dict, seed=7).equals(expected_result)

    # Test case 9
    vegetable_dict = {'Carrot': 10, 'Potato': 20, 'Tomato': 30, 'Cabbage': 40, 'Spinach': 50}
    expected_result = pd.DataFrame({'Count': [10, 20, 30, 40, 50], 'Percentage': [10.0, 20.0, 30.0, 40.0, 50.0]}, index=VEGETABLES)
    assert task_func(vegetable_dict, seed=8).equals(expected_result)

    # Test case 10
    vegetable_dict = {'Carrot': 10, 'Potato': 20, 'Tomato': 30, 'Cabbage': 40, 'Spinach': 50}
    expected_result = pd.DataFrame({'Count': [10, 20, 30, 40, 50], 'Percentage': [10.0, 20.0, 30.0, 40.0, 50.0]}, index=VEGETABLES)
    assert task_func(vegetable_dict, seed=9).equals(expected_result)