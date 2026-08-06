import pytest
from src_0642 import task_func

def test_task_func():
    pattern = r'^[a-zA-Z0-9]+\.txt$'
    directory = 'path/to/directory'
    output_csv = 'output.csv'

    df = task_func(pattern, directory, output_csv)

    assert df.shape[0] > 0
    assert df.columns[0] == 'File Path'
    assert df.dtypes[0] == object
    assert df.iloc[0, 0].startswith(directory)
    assert df.iloc[0, 0].endswith('.txt')

    with open(output_csv, 'r') as f:
        assert f.readline() == 'File Path\n'
        assert f.readline() == df.iloc[0, 0] + '\n'