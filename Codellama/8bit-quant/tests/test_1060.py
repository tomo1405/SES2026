import itertools

import pandas as pd
from src_1060 import task_func


def test_task_func():
    # Test that the function returns a DataFrame
    assert isinstance(task_func(), pd.DataFrame)

    # Test that the DataFrame has the correct shape
    assert task_func().shape == (len(PLANETS), len(ELEMENTS))

    # Test that the DataFrame has the correct column headers
    assert task_func().columns.tolist() == ELEMENTS

    # Test that the DataFrame has the correct values
    expected_values = [
        f"{planet}:{element}"
        for planet, element in itertools.product(PLANETS, ELEMENTS)
    ]
    assert task_func().values.tolist() == expected_values