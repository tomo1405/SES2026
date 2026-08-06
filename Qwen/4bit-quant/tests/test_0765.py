import csv
import os

import pytest
from src_0765 import task_func


def test_task_func_default_parameters():
    csv_file_path = task_func()
    assert os.path.exists(csv_file_path)
    with open(csv_file_path, 'r', encoding='latin-1') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
        assert len(rows) == 50
        for row in rows:
            assert row['Name'] in ['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz', 'Smith', 'Johnson', 'Williams', 'Brown', 'Jones']
            assert 20 <= int(row['Age']) <= 50
    os.remove(csv_file_path)

def test_task_func_custom_parameters():
    custom_csv_file_path = 'custom_names.csv'
    custom_latin_names = ['Doe', 'Lee', 'Kim']
    custom_names = ['Davis', 'Miller', 'Wilson']
    csv_file_path = task_func(custom_csv_file_path, custom_latin_names, custom_names)
    assert os.path.exists(csv_file_path)
    with open(csv_file_path, 'r', encoding='latin-1') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
        assert len(rows) == 50
        for row in rows:
            assert row['Name'] in custom_latin_names + custom_names
            assert 20 <= int(row['Age']) <= 50
    os.remove(csv_file_path)

def test_task_func_invalid_csv_file_type():
    with pytest.raises(TypeError):
        task_func(csv_file=123)

def test_task_func_invalid_names_type():
    with pytest.raises(TypeError):
        task_func(names='not_a_list')

def test_task_func_invalid_latin_names_type():
    with pytest.raises(TypeError):
        task_func(latin_names='not_a_list')

def test_task_func_with_rng_seed():
    csv_file_path_1 = task_func(rng_seed=42)
    csv_file_path_2 = task_func(rng_seed=42)
    with open(csv_file_path_1, 'r', encoding='latin-1') as csvfile1:
        rows1 = list(csv.DictReader(csvfile1))
    with open(csv_file_path_2, 'r', encoding='latin-1') as csvfile2:
        rows2 = list(csv.DictReader(csvfile2))
    assert rows1 == rows2
    os.remove(csv_file_path_1)
    os.remove(csv_file_path_2)