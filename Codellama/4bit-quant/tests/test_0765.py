import csv

import pytest
from src_0765 import task_func


def test_task_func():
    # Test that the function raises a TypeError if csv_file is not a string
    with pytest.raises(TypeError):
        task_func(csv_file=123)

    # Test that the function raises a TypeError if names is not a list
    with pytest.raises(TypeError):
        task_func(names='Smith')

    # Test that the function raises a TypeError if latin_names is not a list
    with pytest.raises(TypeError):
        task_func(latin_names='Sopetón')

    # Test that the function returns the correct csv_file
    csv_file = task_func(csv_file='names.csv', names=['Smith', 'Johnson', 'Williams', 'Brown', 'Jones'], latin_names=['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz'])
    assert csv_file == 'names.csv'

    # Test that the function writes the correct data to the csv file
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        rows = [row for row in reader]
        assert len(rows) == 50
        for row in rows:
            assert row['Name'] in ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones']
            assert row['Age'] in range(20, 50)

    # Test that the function uses the correct encoding
    csv_file = task_func(csv_file='names.csv', names=['Smith', 'Johnson', 'Williams', 'Brown', 'Jones'], latin_names=['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz'], encoding='latin-1')
    with open(csv_file, 'r', encoding='latin-1') as f:
        reader = csv.DictReader(f)
        rows = [row for row in reader]
        assert len(rows) == 50
        for row in rows:
            assert row['Name'] in ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones']
            assert row['Age'] in range(20, 50)

    # Test that the function uses the correct random seed
    csv_file = task_func(csv_file='names.csv', names=['Smith', 'Johnson', 'Williams', 'Brown', 'Jones'], latin_names=['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz'], rng_seed=123)
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        rows = [row for row in reader]
        assert len(rows) == 50
        for row in rows:
            assert row['Name'] in ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones']
            assert row['Age'] in range(20, 50)