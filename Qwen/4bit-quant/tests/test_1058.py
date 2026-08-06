import pandas as pd
from src_1058 import task_func


def test_task_func_default_values():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (10, 7)
    assert list(df.columns) == ["Meat", "Fish", "Grass", "Fruits", "Insects", "Seeds", "Leaves"]
    assert df.iloc[0, 0] == "Dog:Meat"
    assert df.iloc[-1, -1] == "Kangaroo:Leaves"

def test_task_func_custom_animals_and_foods():
    animals = ["Dog", "Cat"]
    foods = ["Meat", "Fish"]
    df = task_func(animals, foods)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)
    assert list(df.columns) == ["Meat", "Fish"]
    assert df.iloc[0, 0] == "Dog:Meat"
    assert df.iloc[-1, -1] == "Cat:Fish"

def test_task_func_empty_animals():
    df = task_func([], ["Meat", "Fish"])
    assert isinstance(df, pd.DataFrame)
    assert df.empty

def test_task_func_empty_foods():
    df = task_func(["Dog", "Cat"], [])
    assert isinstance(df, pd.DataFrame)
    assert df.empty

def test_task_func_both_empty():
    df = task_func([], [])
    assert isinstance(df, pd.DataFrame)
    assert df.empty

def test_task_func_single_animal_single_food():
    df = task_func(["Dog"], ["Meat"])
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (1, 1)
    assert list(df.columns) == ["Meat"]
    assert df.iloc[0, 0] == "Dog:Meat"