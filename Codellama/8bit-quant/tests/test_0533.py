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
    df = pd.DataFrame({"value": [1, 1, 1, 1]})
    duplicates_counter, ax = task_func(df)
    assert duplicates_counter == Counter({1: 4})
    assert ax.get_xlabel() == "Value"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Distribution"

    # Test case 3: Non-constant dataframe
    df = pd.DataFrame({"value": [1, 2, 3, 4, 5]})
    duplicates_counter, ax = task_func(df)
    assert duplicates_counter == Counter()
    assert ax.get_xlabel() == "Value"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Distribution"

    # Test case 4: Non-constant dataframe with duplicates
    df = pd.DataFrame({"value": [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]})
    duplicates_counter, ax = task_func(df)
    assert duplicates_counter == Counter({1: 2, 2: 2, 3: 2, 4: 2, 5: 2})
    assert ax.get_xlabel() == "Value"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Distribution"