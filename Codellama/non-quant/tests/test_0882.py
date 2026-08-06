import pytest
from src_0882 import task_func

def test_task_func_with_valid_inputs():
    csv_file = "data.csv"
    column_name = "data"
    pattern = "\d+[xX]"
    sample_size = 10
    seed = 42

    matches = task_func(csv_file, column_name, pattern, sample_size, seed)

    assert isinstance(matches, pd.DataFrame)
    assert len(matches) == sample_size
    assert all(matches[column_name].str.contains(pattern))

def test_task_func_with_invalid_inputs():
    csv_file = "data.csv"
    column_name = "data"
    pattern = "\d+[xX]"
    sample_size = 10
    seed = 42

    with pytest.raises(ValueError):
        task_func(csv_file, column_name, pattern, sample_size, seed)

def test_task_func_with_invalid_column_name():
    csv_file = "data.csv"
    column_name = "invalid_column"
    pattern = "\d+[xX]"
    sample_size = 10
    seed = 42

    with pytest.raises(KeyError):
        task_func(csv_file, column_name, pattern, sample_size, seed)

def test_task_func_with_invalid_pattern():
    csv_file = "data.csv"
    column_name = "data"
    pattern = "invalid_pattern"
    sample_size = 10
    seed = 42

    with pytest.raises(ValueError):
        task_func(csv_file, column_name, pattern, sample_size, seed)

def test_task_func_with_invalid_sample_size():
    csv_file = "data.csv"
    column_name = "data"
    pattern = "\d+[xX]"
    sample_size = 1000
    seed = 42

    with pytest.raises(ValueError):
        task_func(csv_file, column_name, pattern, sample_size, seed)

def test_task_func_with_invalid_seed():
    csv_file = "data.csv"
    column_name = "data"
    pattern = "\d+[xX]"
    sample_size = 10
    seed = "invalid_seed"

    with pytest.raises(TypeError):
        task_func(csv_file, column_name, pattern, sample_size, seed)