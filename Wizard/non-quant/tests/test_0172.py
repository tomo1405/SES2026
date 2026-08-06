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

# Test the function
def test_task_func():
    # Test case 1
    vegetable_dict = {'Carrot': 0.5, 'Potato': 0.3, 'Tomato': 0.2, 'Cabbage': 0.1, 'Spinach': 0.1}
    expected_result = pd.DataFrame({'Count': [1, 2, 3, 4, 5], 'Percentage': [50.0, 30.0, 20.0, 10.0, 10.0]}, index=VEGETABLES)
    assert task_func(vegetable_dict).equals(expected_result)

    # Test case 2
    vegetable_dict = {'Carrot': 0.5, 'Potato': 0.3, 'Tomato': 0.2, 'Cabbage': 0.1, 'Spinach': 0.1}
    expected_result = pd.DataFrame({'Count': [1, 2, 3, 4, 5], 'Percentage': [50.0, 30.0, 20.0, 10.0, 10.0]}, index=VEGETABLES)
    assert task_func(vegetable_dict).equals(expected_result)

    # Test case 3
    vegetable_dict = {'Carrot': 0.5, 'Potato': 0.3, 'Tomato': 0.2, 'Cabbage': 0.1, 'Spinach': 0.1}
    expected_result = pd.DataFrame({'Count': [1, 2, 3, 4, 5], 'Percentage': [50.0, 30.0, 20.0, 10.0, 10.0]}, index=VEGETABLES)
    assert task_func(vegetable_dict).equals(expected_result)

    # Test case 4
    vegetable_dict = {'Carrot': 0.5, 'Potato': 0.3, 'Tomato': 0.2, 'Cabbage': 0.1, 'Spinach': 0.1}
    expected_result = pd.DataFrame({'Count': [1, 2, 3, 4, 5], 'Percentage': [50.0, 30.0, 20.0, 10.0, 10.0]}, index=VEGETABLES)
    assert task_func(vegetable_dict).equals(expected_result)

    # Test case 5
    vegetable_dict = {'Carrot': 0.5, 'Potato': 0.3, 'Tomato': 0.2, 'Cabbage': 0.1, 'Spinach': 0.1}
    expected_result = pd.DataFrame({'Count': [1, 2, 3, 4, 5], 'Percentage': [50.0, 30.0, 20.0, 10.0, 10.0]}, index=VEGETABLES)
    assert task_func(vegetable_dict).equals(expected_result)

    # Test case 6
    vegetable_dict = {'Carrot': 0.5, 'Potato': 0.3, 'Tomato': 0.2, 'Cabbage': 0.1, 'Spinach': 0.1}
    expected_result = pd.DataFrame({'Count': [1, 2, 3, 4, 5], 'Percentage': [50.0, 30.0, 20.0, 10.0, 10.0]}, index=VEGETABLES)
    assert task_func(vegetable_dict).equals(expected_result)

    # Test case 7
    vegetable_dict = {'Carrot': 0.5, 'Potato': 0.3, 'Tomato': 0.2, 'Cabbage': 0.1, 'Spinach': 0.1}
    expected_result = pd.DataFrame({'Count': [1, 2, 3, 4, 5], 'Percentage': [50.0, 30.0, 20.0, 10.0, 10.0]}, index=VEGETABLES)
    assert task_func(vegetable_dict).equals(expected_result)

    # Test case 8
    vegetable_dict = {'Carrot': 0.5, 'Potato': 0.3, 'Tomato': 0.2, 'Cabbage': 0.1, 'Spinach': 0.1}
    expected_result = pd.DataFrame({'Count': [1, 2, 3, 4, 5], 'Percentage': [50.0, 30.0, 20.0, 10.0, 10.0]}, index=VEGETABLES)
    assert task_func(vegetable_dict).equals(expected_result)

    # Test case 9
    vegetable_dict = {'Carrot': 0.5, 'Potato': 0.3, 'Tomato': 0.2, 'Cabbage': 0.1, 'Spinach': 0.1}
    expected_result = pd.DataFrame({'Count': [1, 2, 3, 4, 5], 'Percentage': [50.0, 30.0, 20.0, 10.0, 10.0]}, index=VEGETABLES)
    assert task_func(vegetable_dict).equals(expected_result)

    # Test case 10
    vegetable_dict = {'Carrot': 0.5, 'Potato': 0.3, 'Tomato': 0.2, 'Cabbage': 0.1, 'Spinach': 0.1}
    expected_result = pd.DataFrame({'Count': [1, 2, 3, 4, 5], 'Percentage': [50.0, 30.0, 20.0, 10.0, 10.0]}, index=VEGETABLES)
    assert task_func(vegetable_dict).equals(expected_result)

test_task_func()