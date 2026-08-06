python
import os
import random
import pandas as pd
import pytest

def task_func(data_dir,
          csv_files=['file1.csv', 'file2.csv', 'file3.csv'],
          seed=None):

    random.seed(seed)

    file = csv_files[random.randint(0, len(csv_files) - 1)]
    file_path = os.path.join(data_dir, file)

    try:
        df = pd.read_csv(file_path)
    except pd.errors.EmptyDataError:
        return file, pd.DataFrame()

    selected_rows = df.sample(n=random.randint(1, len(df)), random_state=seed)

    return file, selected_rows

def test_task_func():
    # Test case 1: Valid data directory and seed
    data_dir = 'data'
    seed = 42
    expected_file = 'file2.csv'
    expected_selected_rows = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})

    file, selected_rows = task_func(data_dir, seed=seed)

    assert file == expected_file
    assert selected_rows.equals(expected_selected_rows)

    # Test case 2: Invalid data directory
    data_dir = 'invalid_data'
    seed = 42

    with pytest.raises(FileNotFoundError):
        task_func(data_dir, seed=seed)

    # Test case 3: Empty data frame
    data_dir = 'data'
    seed = 100

    file, selected_rows = task_func(data_dir, seed=seed)

    assert file == 'file3.csv'
    assert selected_rows.empty