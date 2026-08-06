from collections import Counter

import pandas as pd
from src_0533 import task_func


def test_task_func():
    # Test case 1: Empty dataframe
    df = pd.DataFrame()
    duplicates_counter, ax = task_func(df)
    assert duplicates_counter == Counter()
    assert ax.get_xlabel() == "Value"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Distribution"

    # Test case 2: Constant dataframe
    df = pd.DataFrame({"value": [1, 1, 1, 1, 1]})
    duplicates_counter, ax = task_func(df)
    assert duplicates_counter == Counter()
    assert ax.get_xlabel() == "Value"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Distribution"

    # Test case 3: Non-empty dataframe with duplicates
    df = pd.DataFrame({"value": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
    duplicates_counter, ax = task_func(df)
    assert duplicates_counter == Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1})
    assert ax.get_xlabel() == "Value"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Distribution"

    # Test case 4: Non-empty dataframe without duplicates
    df = pd.DataFrame({"value": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
    duplicates_counter, ax = task_func(df, bins=10)
    assert duplicates_counter == Counter()
    assert ax.get_xlabel() == "Value"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Distribution"

    # Test case 5: Non-empty dataframe with duplicates and custom bins
    df = pd.DataFrame({"value": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
    duplicates_counter, ax = task_func(df, bins=5)
    assert duplicates_counter == Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1})
    assert ax.get_xlabel() == "Value"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Distribution"