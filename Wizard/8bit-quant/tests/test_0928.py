python
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pytest

def task_func(file_path: str, column_name: str) -> pd.DataFrame:
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Replace occurrences of '\n' with '<br>'
    df[column_name] = df[column_name].replace({'\n': '<br>'}, regex=True)
    
    # Initialize LabelEncoder and fit_transform the specified column
    le = LabelEncoder()
    df[column_name] = le.fit_transform(df[column_name])
    
    return df

def test_task_func():
    # Test case 1: Test with valid input
    df = task_func('test_data.csv', 'text_column')
    assert df.shape == (10, 2)
    assert df['text_column'].dtype == 'int64'
    
    # Test case 2: Test with invalid input (file not found)
    with pytest.raises(FileNotFoundError):
        task_func('invalid_file.csv', 'text_column')
    
    # Test case 3: Test with invalid input (column not found)
    with pytest.raises(KeyError):
        task_func('test_data.csv', 'invalid_column')