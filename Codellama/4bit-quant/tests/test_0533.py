from typing import Counter

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

    # Test case 2: Dataframe with constant values
    df = pd.DataFrame({"value": [1, 1, 1, 1]})
    duplicates_counter, ax = task_func(df)
    assert duplicates_counter == Counter()
    assert ax.get_xlabel() == "Value"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Distribution"

    # Test case 3: Dataframe with duplicate values
    df = pd.DataFrame({"value": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
    duplicates_counter, ax = task_func(df)
    assert duplicates_counter == Counter({1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2, 10: 2})
    assert ax.get_xlabel() == "Value"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Distribution"

    # Test case 4: Dataframe with non-duplicate values
    df = pd.DataFrame({"value": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
    duplicates_counter, ax = task_func(df)
    assert duplicates_counter == Counter()
    assert ax.get_xlabel() == "Value"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Distribution"

    # Test case 5: Dataframe with non-numeric values
    df = pd.DataFrame({"value": ["a", "b", "c", "d", "e"]})
    duplicates_counter, ax = task_func(df)
    assert duplicates_counter == Counter()
    assert ax.get_xlabel() == "Value"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Distribution"