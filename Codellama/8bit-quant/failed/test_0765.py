import pytest
from src_0765 import task_func

def test_task_func_type_error():
    with pytest.raises(TypeError):
        task_func(csv_file=123)

def test_task_func_type_error_names():
    with pytest.raises(TypeError):
        task_func(names=123)

def test_task_func_type_error_latin_names():
    with pytest.raises(TypeError):
        task_func(latin_names=123)

def test_task_func_type_error_encoding():
    with pytest.raises(TypeError):
        task_func(encoding=123)

def test_task_func_type_error_rng_seed():
    with pytest.raises(TypeError):
        task_func(rng_seed=123)

def test_task_func_value_error_csv_file():
    with pytest.raises(ValueError):
        task_func(csv_file='')

def test_task_func_value_error_names():
    with pytest.raises(ValueError):
        task_func(names=[])

def test_task_func_value_error_latin_names():
    with pytest.raises(ValueError):
        task_func(latin_names=[])

def test_task_func_value_error_encoding():
    with pytest.raises(ValueError):
        task_func(encoding='')

def test_task_func_value_error_rng_seed():
    with pytest.raises(ValueError):
        task_func(rng_seed='')

def test_task_func_return_value():
    assert task_func(csv_file='names.csv', names=['Smith', 'Johnson', 'Williams', 'Brown', 'Jones'], encoding='latin-1') == 'names.csv'

def test_task_func_return_value_latin_names():
    assert task_func(csv_file='names.csv', latin_names=['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz'], encoding='latin-1') == 'names.csv'

def test_task_func_return_value_rng_seed():
    assert task_func(csv_file='names.csv', names=['Smith', 'Johnson', 'Williams', 'Brown', 'Jones'], encoding='latin-1', rng_seed=123) == 'names.csv'

def test_task_func_return_value_latin_names_rng_seed():
    assert task_func(csv_file='names.csv', latin_names=['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz'], encoding='latin-1', rng_seed=123) == 'names.csv'