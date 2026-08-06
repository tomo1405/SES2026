import pytest
from src_0882 import task_func

def test_task_func():
    csv_file = 'path/to/csv/file.csv'
    column_name = 'data'
    pattern = '\d+[xX]'
    sample_size = 10
    seed = 42

    matches = task_func(csv_file, column_name, pattern, sample_size, seed)

    assert isinstance(matches, pd.DataFrame)
    assert len(matches) == sample_size
    assert matches[column_name].str.contains(pattern).all()