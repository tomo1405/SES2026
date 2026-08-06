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
    fruit_data = []
    expected_report = pd.DataFrame()
    assert task_func(fruit_data).equals(expected_report)

    # Test case 2: List with one fruit
    fruit_data = [('apple', 5), ('banana', 3)]
    expected_report = pd.DataFrame({'Total Count': [5, 3], 'Average Count': [5, 3]}, index=['apple', 'banana'])
    assert task_func(fruit_data).equals(expected_report)

    # Test case 3: List with multiple fruits
    fruit_data = [('apple', 5), ('banana', 3), ('apple', 2), ('orange', 4)]
    expected_report = pd.DataFrame({'Total Count': [7, 3, 4], 'Average Count': [7/2, 3, 4]}, index=['apple', 'banana', 'orange'])
    assert task_func(fruit_data).equals(expected_report)