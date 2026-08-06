import pandas as pd
import pytest
from src_1058 import task_func


def test_task_func():
    # Test with default arguments
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (10, 7)
    assert list(df.columns) == ["Meat", "Fish", "Grass", "Fruits", "Insects", "Seeds", "Leaves"]

    # Test with custom arguments
    df = task_func(animals=["Lion", "Tiger"], foods=["Meat", "Fish"])
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)
    assert list(df.columns) == ["Meat", "Fish"]

def test_task_func_empty_lists():
    # Test with empty lists
    df = task_func(animals=[], foods=[])
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (0, 0)

def test_task_func_invalid_input():
    # Test with invalid input
    with pytest.raises(ValueError):
        task_func(animals="invalid", foods="invalid")