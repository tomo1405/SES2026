import pytest
from src_0765 import task_func
import os
import csv

def test_task_func_default_behavior(tmp_path):
    csv_file_path = tmp_path / "test_names.csv"
    result = task_func(str(csv_file_path))
    assert result == str(csv_file_path)
    assert os.path.exists(csv_file_path)

    with open(csv_file_path, mode='r', newline='', encoding='latin-1') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        assert len(rows) == 50
        for row in rows:
            assert 'Name' in row
            assert 'Age' in row
            assert int(row['Age']) >= 20 and int(row['Age']) <= 50

def test_task_func_with_custom_names_and_latin_names(tmp_path):
    csv_file_path = tmp_path / "custom_names.csv"
    custom_names = ['Doe', 'Smith', 'Brown']
    custom_latin_names = ['Martínez', 'Rodríguez', 'Hernández']
    result = task_func(str(csv_file_path), names=custom_names, latin_names=custom_latin_names)
    assert result == str(csv_file_path)
    assert os.path.exists(csv_file_path)

    with open(csv_file_path, mode='r', newline='', encoding='latin-1') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        assert len(rows) == 50
        for row in rows:
            assert row['Name'] in custom_names + custom_latin_names
            assert int(row['Age']) >= 20 and int(row['Age']) <= 50

def test_task_func_with_rng_seed(tmp_path):
    csv_file_path = tmp_path / "seeded_names.csv"
    seed_value = 42
    result = task_func(str(csv_file_path), rng_seed=seed_value)
    assert result == str(csv_file_path)
    assert os.path.exists(csv_file_path)

    with open(csv_file_path, mode='r', newline='', encoding='latin-1') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        assert len(rows) == 50
        for row in rows:
            assert 'Name' in row
            assert 'Age' in row
            assert int(row['Age']) >= 20 and int(row['Age']) <= 50

def test_task_func_invalid_csv_file_type():
    with pytest.raises(TypeError):
        task_func(123)

def test_task_func_invalid_names_type():
    with pytest.raises(TypeError):
        task_func(names="Not a list")

def test_task_func_invalid_latin_names_type():
    with pytest.raises(TypeError):
        task_func(latin_names="Not a list")