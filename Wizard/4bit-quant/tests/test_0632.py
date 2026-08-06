python
import csv
import os
import pytest

from src_0632 import task_func

def test_task_func():
    # Test case 1: Test with default output directory
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': ['a', 'b', 'c']})
    filename = 'test.csv'
    file_path = task_func(df, filename)
    assert os.path.exists(file_path)
    assert os.path.isfile(file_path)
    assert os.path.basename(file_path) == filename
    assert os.path.dirname(file_path) == os.path.abspath(OUTPUT_DIR)

    # Test case 2: Test with custom output directory
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': ['a', 'b', 'c']})
    filename = 'test.csv'
    output_dir = './custom_output'
    file_path = task_func(df, filename, output_dir=output_dir)
    assert os.path.exists(file_path)
    assert os.path.isfile(file_path)
    assert os.path.basename(file_path) == filename
    assert os.path.dirname(file_path) == os.path.abspath(output_dir)

    # Test case 3: Test with invalid dataframe
    df = 'invalid dataframe'
    filename = 'test.csv'
    with pytest.raises(TypeError):
        task_func(df, filename)

    # Test case 4: Test with invalid filename
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': ['a', 'b', 'c']})
    filename = 1234
    with pytest.raises(TypeError):
        task_func(df, filename)

    # Test case 5: Test with invalid output directory
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': ['a', 'b', 'c']})
    filename = 'test.csv'
    output_dir = 1234
    with pytest.raises(TypeError):
        task_func(df, filename, output_dir=output_dir)