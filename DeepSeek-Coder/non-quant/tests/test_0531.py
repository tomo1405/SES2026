import pytest
from src_0531 import task_func
import pandas as pd
import numpy as np
from collections import Counter
import seaborn as sns
import matplotlib.pyplot as plt

# Test cases for task_func
def test_task_func():
    # Test case 1: Normal case
    data = {
        "name": ["Alice", "Bob", "Alice", "Charlie", "Bob"],
        "age": [25, 30, 25, 35, 30]
    }
    df = pd.DataFrame(data)
    expected_counter = Counter({25: 2, 30: 2})
    expected_ax = None
    result_counter, result_ax = task_func(df)
    assert result_counter == expected_counter
    assert result_ax is None

    # Test case 2: Empty DataFrame
    df_empty = pd.DataFrame(columns=["name", "age"])
    with pytest.raises(ValueError):
        task_func(df_empty)

    # Test case 3: Negative age
    data = {
        "name": ["Alice", "Bob", "Alice", "Charlie", "Bob"],
        "age": [25, 30, 25, 35, 30]
    }
    df_negative_age = pd.DataFrame(data)
    with pytest.raises(ValueError):
        task_func(df_negative_age)

    # Test case 4: No duplicates
    data = {
        "name": ["Alice", "Bob", "Charlie"],
        "age": [25, 30, 35]
    }
    df_no_duplicates = pd.DataFrame(data)
    result_counter, result_ax = task_func(df_no_duplicates)
    assert result_counter == Counter()
    assert result_ax is None