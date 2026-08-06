import csv
import random
from src_0765 import task_func

def test_task_func_with_latin_names():
    csv_file = task_func(latin_names=['Foo', 'Bar', 'Baz'])
    with open(csv_file, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            assert row['Name'] in ['Foo', 'Bar', 'Baz']

def test_task_func_with_names():
    csv_file = task_func(names=['Alice', 'Bob', 'Charlie'])
    with open(csv_file, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            assert row['Name'] in ['Alice', 'Bob', 'Charlie']

def test_task_func_with_invalid_csv_file():
    with pytest.raises(TypeError):
        task_func(csv_file=123)

def test_task_func_with_invalid_names():
    with pytest.raises(TypeError):
        task_func(names='foo')

def test_task_func_with_invalid_latin_names():
    with pytest.raises(TypeError):
        task_func(latin_names=123)

def test_task_func_with_invalid_encoding():
    with pytest.raises(TypeError):
        task_func(encoding=123)

def test_task_func_with_invalid_rng_seed():
    with pytest.raises(TypeError):
        task_func(rng_seed='foo')