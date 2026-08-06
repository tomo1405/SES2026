import pytest
from src_1058 import task_func

def test_task_func_default_values():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == ["Meat", "Fish", "Grass", "Fruits", "Insects", "Seeds", "Leaves"]
    assert df.shape == (10, 7)

def test_task_func_custom_animals_and_foods():
    animals = ["Dog", "Cat"]
    foods = ["Meat", "Fish"]
    df = task_func(animals, foods)
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == ["Meat", "Fish"]
    assert df.shape == (2, 2)

def test_task_func_empty_animals():
    df = task_func(animals=[])
    assert isinstance(df, pd.DataFrame)
    assert df.empty

def test_task_func_empty_foods():
    df = task_func(foods=[])
    assert isinstance(df, pd.DataFrame)
    assert df.empty

def test_task_func_no_animals_no_foods():
    df = task_func(animals=[], foods=[])
    assert isinstance(df, pd.DataFrame)
    assert df.empty

def test_task_func_single_animal():
    df = task_func(animals=["Dog"])
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == ["Meat", "Fish", "Grass", "Fruits", "Insects", "Seeds", "Leaves"]
    assert df.shape == (1, 7)

def test_task_func_single_food():
    df = task_func(foods=["Meat"])
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == ["Meat"]
    assert df.shape == (10, 1)