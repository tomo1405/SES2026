import pandas as pd
import itertools
import numpy as np
from src_1058 import task_func

def test_task_func():
    # Test with default arguments
    df = task_func()
    expected_columns = ["Meat", "Fish", "Grass", "Fruits", "Insects", "Seeds", "Leaves"]
    assert df.columns.tolist() == expected_columns
    expected_data = np.array([f"{a}:{f}" for a, f in itertools.product(
        ["Dog", "Cat", "Elephant", "Tiger", "Lion", "Zebra", "Giraffe", "Bear", "Monkey", "Kangaroo"],
        ["Meat", "Fish", "Grass", "Fruits", "Insects", "Seeds", "Leaves"]
    )]).reshape(-1, len(expected_columns))
    assert df.values.tolist() == expected_data.tolist()

    # Test with custom arguments
    df = task_func(animals=["Dog", "Cat"], foods=["Meat", "Fish"])
    expected_columns = ["Meat", "Fish"]
    assert df.columns.tolist() == expected_columns
    expected_data = np.array([f"{a}:{f}" for a, f in itertools.product(
        ["Dog", "Cat"],
        ["Meat", "Fish"]
    )]).reshape(-1, len(expected_columns))
    assert df.values.tolist() == expected_data.tolist()

    # Test with empty lists
    df = task_func(animals=[], foods=[])
    assert df.empty

    # Test with None as an argument
    df = task_func(animals=None, foods=None)
    assert df.empty