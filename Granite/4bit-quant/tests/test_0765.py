import csv
import random

from src_0765 import task_func


def test_task_func():
    csv_file = 'names.csv'
    latin_names = ['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz']
    names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones']
    encoding = 'latin-1'
    rng_seed = None

    with open(csv_file, 'w', newline='', encoding=encoding) as csvfile:
        fieldnames = ['Name', 'Age']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(50):
            if latin_names:
                writer.writerow({'Name': random.choice(latin_names), 'Age': random.randint(20, 50)})
            if names:
                writer.writerow({'Name': random.choice(names), 'Age': random.randint(20, 50)})

    assert task_func(csv_file, latin_names, names, encoding, rng_seed) == 'names.csv'