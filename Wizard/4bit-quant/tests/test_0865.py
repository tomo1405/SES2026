python
import pandas as pd
import numpy as np
import pytest

def task_func(fruit_data):

    if len(fruit_data) == 0:
        return pd.DataFrame()

    # Unpacking the fruit names and counts separately
    fruits, counts = zip(*fruit_data)
    fruits = unique_values = list(set(fruits))
    # Calculating total counts
    total_counts = {fruit: np.sum([count for fruit_, count in fruit_data if fruit_ == fruit])
                  for fruit in fruits}
    # Calculating average counts
    avg_counts = {fruit: np.mean([count for fruit_, count in fruit_data if fruit_ == fruit])
                  for fruit in fruits}

    # Creating a DataFrame to hold the report
    report_df = pd.DataFrame(list(zip(total_counts.values(), avg_counts.values())),
                             index=fruits,
                             columns=['Total Count', 'Average Count'])

    return report_df

def test_task_func():
    # Test case 1: Empty list
    assert task_func([]) == pd.DataFrame()

    # Test case 2: List with one fruit
    fruit_data = [('Apple', 10), ('Banana', 5)]
    expected_report = pd.DataFrame({'Total Count': [10], 'Average Count': [5]}, index=['Apple'])
    assert task_func(fruit_data).equals(expected_report)

    # Test case 3: List with multiple fruits
    fruit_data = [('Apple', 10), ('Banana', 5), ('Apple', 20), ('Orange', 15)]
    expected_report = pd.DataFrame({'Total Count': [30, 15], 'Average Count': [15, 15]}, index=['Apple', 'Orange'])
    assert task_func(fruit_data).equals(expected_report)