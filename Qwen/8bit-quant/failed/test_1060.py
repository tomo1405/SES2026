import pytest
from src_1060 import task_func
import numpy as np
import pandas as pd

def test_task_func():
    # Call the function
    df = task_func()

    # Check that the DataFrame has the correct shape
    assert df.shape == (len(PLANETS), len(ELEMENTS))

    # Check that the column headers are correct
    assert list(df.columns) == ELEMENTS

    # Check that each row corresponds to a planet and each column to an element
    for i, planet in enumerate(PLANETS):
        for j, element in enumerate(ELEMENTS):
            expected_value = f"{planet}:{element}"
            assert df.iloc[i, j] == expected_value

    # Check that the DataFrame is shuffled
    # This is a bit tricky because we can't predict the exact order, but we can check that it's not sorted
    original_pairs = [f"{planet}:{element}" for planet, element in itertools.product(PLANETS, ELEMENTS)]
    shuffled_pairs = df.values.flatten().tolist()
    assert shuffled_pairs != original_pairs