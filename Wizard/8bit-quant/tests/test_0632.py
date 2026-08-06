python
import csv
import os
import pytest

OUTPUT_DIR = './output'

def task_func(df, filename, output_dir=OUTPUT_DIR):
    # Ensure the data directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    file_path = os.path.join(output_dir, filename)
    df.to_csv(file_path, index=False, quoting=csv.QUOTE_NONNUMERIC)
    return os.path.abspath(file_path)

def test_task_func():
    # Test case 1: Test with valid input
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': ['a', 'b', 'c']})
    filename = 'test.csv'
    file_path = task_func(df, filename)
    assert os.path.exists(file_path)
    os.remove(file_path)

    # Test case 2: Test with invalid input
    with pytest.raises(TypeError):
        task_func('not a dataframe', 'test.csv')

    with pytest.raises(TypeError):
        task_func(df, 123)

    with pytest.raises(TypeError):
        task_func(df, 'test.csv', output_dir=123)