import pytest
from src_0765 import task_func

def test_task_func_type_error():
    with pytest.raises(TypeError):
        task_func(csv_file=123, names=['Smith', 'Johnson', 'Williams', 'Brown', 'Jones'])

def test_task_func_type_error_latin_names():
    with pytest.raises(TypeError):
        task_func(csv_file='names.csv', latin_names=123, names=['Smith', 'Johnson', 'Williams', 'Brown', 'Jones'])

def test_task_func_type_error_names():
    with pytest.raises(TypeError):
        task_func(csv_file='names.csv', latin_names=['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz'], names=123)

def test_task_func_type_error_rng_seed():
    with pytest.raises(TypeError):
        task_func(csv_file='names.csv', latin_names=['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz'], names=['Smith', 'Johnson', 'Williams', 'Brown', 'Jones'], rng_seed='abc')

def test_task_func_return_value():
    assert task_func(csv_file='names.csv', latin_names=['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz'], names=['Smith', 'Johnson', 'Williams', 'Brown', 'Jones']) == 'names.csv'

def test_task_func_return_value_with_rng_seed():
    assert task_func(csv_file='names.csv', latin_names=['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz'], names=['Smith', 'Johnson', 'Williams', 'Brown', 'Jones'], rng_seed=123) == 'names.csv'