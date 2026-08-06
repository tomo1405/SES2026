import pytest
from src_0396 import task_func

def test_task_func():
    # Test that the function raises an error if the directory does not exist
    with pytest.raises(FileNotFoundError):
        task_func(directory='/path/to/nonexistent/directory')

    # Test that the function raises an error if no files are found matching the pattern
    with pytest.raises(ValueError):
        task_func(directory='./', file_pattern='*.nonexistent')

    # Test that the function returns a DataFrame with the correct columns
    df = task_func(directory='./', file_pattern='*.txt')
    assert isinstance(df, pd.DataFrame)
    assert df.columns.tolist() == ['Filename', 'Numeric Data']

    # Test that the function extracts the correct numeric data from a file
    with open('./test_file.txt', 'w') as file:
        file.write('12345')
    df = task_func(directory='./', file_pattern='*.txt')
    assert df.iloc[0]['Numeric Data'] == [12345]

    # Test that the function handles multiple files correctly
    with open('./test_file_1.txt', 'w') as file:
        file.write('12345')
    with open('./test_file_2.txt', 'w') as file:
        file.write('67890')
    df = task_func(directory='./', file_pattern='*.txt')
    assert df.iloc[0]['Numeric Data'] == [12345]
    assert df.iloc[1]['Numeric Data'] == [67890]