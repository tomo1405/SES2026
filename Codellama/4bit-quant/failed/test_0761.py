import pytest
from src_0761 import task_func

def test_task_func():
    # Test that the function returns a pandas DataFrame
    df = task_func()
    assert isinstance(df, pd.DataFrame)

    # Test that the DataFrame has the correct columns
    expected_columns = ['ID', 'Name', 'Date of Birth', 'Email']
    assert list(df.columns) == expected_columns

    # Test that the DataFrame has the correct number of rows
    expected_num_rows = 100
    assert df.shape[0] == expected_num_rows

    # Test that the DataFrame contains the correct data
    expected_data = [
        [1, 'Sopetón', '1980-01-01', 'sopetón1980@example.com'],
        [2, 'Méndez', '1980-01-02', 'méndez1980@example.com'],
        [3, 'Gómez', '1980-01-03', 'gómez1980@example.com'],
        [4, 'Pérez', '1980-01-04', 'pérez1980@example.com'],
        [5, 'Muñoz', '1980-01-05', 'muñoz1980@example.com'],
        [6, 'Smith', '1980-01-06', 'smith1980@example.com'],
        [7, 'Johnson', '1980-01-07', 'johnson1980@example.com'],
        [8, 'Williams', '1980-01-08', 'williams1980@example.com'],
        [9, 'Brown', '1980-01-09', 'brown1980@example.com'],
        [10, 'Jones', '1980-01-10', 'jones1980@example.com']
    ]
    assert df.equals(expected_data)