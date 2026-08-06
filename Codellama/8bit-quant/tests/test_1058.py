import pandas as pd
from src_1058 import task_func


def test_task_func():
    # Test with default lists
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 10
    assert len(df.columns) == 7

    # Test with custom lists
    animals = ["Dog", "Cat", "Elephant"]
    foods = ["Meat", "Fish", "Grass"]
    df = task_func(animals, foods)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 3
    assert len(df.columns) == 3

    # Test with empty lists
    df = task_func([], [])
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 0
    assert len(df.columns) == 0