import csv
import os

import pytest
from src_0765 import task_func


def test_task_func_default_parameters():
    # Test with default parameters
    result = task_func()
    assert os.path.exists(result)
    os.remove(result)

def test_task_func_custom_file_name():
    # Test with a custom file name
    custom_file_name = 'test_names.csv'
    result = task_func(csv_file=custom_file_name)
    assert result == custom_file_name
    assert os.path.exists(result)
    os.remove(result)

def test_task_func_custom_names():
    # Test with custom names
    custom_names = ['Doe', 'Davis']
    result = task_func(names=custom_names)
    assert os.path.exists(result)
    with open(result, 'r', encoding='latin-1') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            assert row['Name'] in custom_names or row['Name'] in ['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz']
    os.remove(result)

def test_task_func_custom_latin_names():
    # Test with custom Latin names
    custom_latin_names = ['Rodríguez', 'López']
    result = task_func(latin_names=custom_latin_names)
    assert os.path.exists(result)
    with open(result, 'r', encoding='latin-1') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            assert row['Name'] in custom_latin_names or row['Name'] in ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones']
    os.remove(result)

def test_task_func_custom_encoding():
    # Test with custom encoding
    custom_encoding = 'utf-8'
    result = task_func(encoding=custom_encoding)
    assert os.path.exists(result)
    with open(result, 'r', encoding=custom_encoding) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            assert 'Name' in row and 'Age' in row
    os.remove(result)

def test_task_func_rng_seed():
    # Test with a specific random seed
    rng_seed = 42
    result = task_func(rng_seed=rng_seed)
    assert os.path.exists(result)
    with open(result, 'r', encoding='latin-1') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
        first_row = rows[0]
    # Repeat with the same seed to ensure consistency
    result2 = task_func(rng_seed=rng_seed)
    with open(result2, 'r', encoding='latin-1') as csvfile2:
        reader2 = csv.DictReader(csvfile2)
        rows2 = list(reader2)
        first_row2 = rows2[0]
    assert first_row == first_row2
    os.remove(result)
    os.remove(result2)

def test_task_func_invalid_csv_file_type():
    # Test with invalid csv_file type
    with pytest.raises(TypeError):
        task_func(csv_file=123)

def test_task_func_invalid_names_type():
    # Test with invalid names type
    with pytest.raises(TypeError):
        task_func(names='not_a_list')

def test_task_func_invalid_latin_names_type():
    # Test with invalid latin_names type
    with pytest.raises(TypeError):
        task_func(latin_names='not_a_list')