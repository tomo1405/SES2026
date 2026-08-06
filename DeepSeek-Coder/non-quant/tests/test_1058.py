import pytest
from src_1058 import task_func

def test_task_func():
    # Test with default parameters
    result = task_func()
    assert isinstance(result, pd.DataFrame)
    assert not result.empty

    # Test with custom animals and foods
    animals = ["Dog", "Cat"]
    foods = ["Meat", "Fish"]
    result = task_func(animals=animals, foods=foods)
    assert isinstance(result, pd.DataFrame)
    assert not result.empty

    # Test with empty lists
    result = task_func([], [])
    assert isinstance(result, pd.DataFrame)
    assert result.empty

    # Test with None parameters
    result = task_func(None, None)
    assert isinstance(result, pd.DataFrame)
    assert not result.empty