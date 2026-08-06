python
import csv
import random
import pytest

def task_func(csv_file='names.csv', 
          latin_names=['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz'],
          names=['Smith', 'Johnson', 'Williams', 'Brown', 'Jones'],
          encoding='latin-1', rng_seed=None):

    if not isinstance(csv_file, str):
        raise TypeError("csv_file should be a string.")
    
    if not isinstance(names, list):
        raise TypeError("names should be a list.")
    
    if not isinstance(latin_names, list):
        raise TypeError("latin_names should be a list.")

    if rng_seed is not None:
        random.seed(rng_seed)

    with open(csv_file, 'w', newline='', encoding=encoding) as csvfile:
        fieldnames = ['Name', 'Age']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(50):
            if latin_names:
                writer.writerow({'Name': random.choice(latin_names), 'Age': random.randint(20, 50)})
            if names:
                writer.writerow({'Name': random.choice(names), 'Age': random.randint(20, 50)})

    return csv_file

def test_task_func():
    # Test case 1: Test with default arguments
    assert task_func() == 'names.csv'

    # Test case 2: Test with custom arguments
    assert task_func(csv_file='custom_names.csv', names=['A', 'B', 'C'], latin_names=['D', 'E', 'F']) == 'custom_names.csv'

    # Test case 3: Test with invalid arguments
    with pytest.raises(TypeError):
        task_func(csv_file=123)

    with pytest.raises(TypeError):
        task_func(names='abc')

    with pytest.raises(TypeError):
        task_func(latin_names='def')

    with pytest.raises(TypeError):
        task_func(encoding=123)

    with pytest.raises(TypeError):
        task_func(rng_seed='abc')