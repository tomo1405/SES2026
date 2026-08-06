import pytest
from src_1058 import task_func

def test_task_func_default_values():
    df = task_func()
    expected_columns = ["Meat", "Fish", "Grass", "Fruits", "Insects", "Seeds", "Leaves"]
    assert list(df.columns) == expected_columns
    assert df.shape[0] == 10  # Number of animals
    assert df.shape[1] == 7  # Number of foods

def test_task_func_custom_animals_and_foods():
    animals = ["A", "B"]
    foods = ["X", "Y"]
    df = task_func(animals, foods)
    expected_columns = ["X", "Y"]
    assert list(df.columns) == expected_columns
    assert df.shape[0] == 2  # Number of animals
    assert df.shape[1] == 2  # Number of foods

def test_task_func_empty_animals():
    df = task_func(animals=[])
    assert df.empty

def test_task_func_empty_foods():
    df = task_func(foods=[])
    assert df.empty

def test_task_func_single_animal_multiple_foods():
    animals = ["A"]
    foods = ["X", "Y", "Z"]
    df = task_func(animals, foods)
    expected_columns = ["X", "Y", "Z"]
    assert list(df.columns) == expected_columns
    assert df.shape[0] == 1  # Number of animals
    assert df.shape[1] == 3  # Number of foods

def test_task_func_multiple_animals_single_food():
    animals = ["A", "B", "C"]
    foods = ["X"]
    df = task_func(animals, foods)
    expected_columns = ["X"]
    assert list(df.columns) == expected_columns
    assert df.shape[0] == 3  # Number of animals
    assert df.shape[1] == 1  # Number of foods