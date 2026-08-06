import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pytest

def task_func(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    le = LabelEncoder()
    df[column_name] = le.fit_transform(df[column_name])
    return df

def test_task_func():
    # Create a sample DataFrame
    df = pd.DataFrame({
        'column_name': ['cat', 'dog', 'mouse', 'cat', 'dog']
    })

    # Test the function with the sample DataFrame
    result_df = task_func(df, 'column_name')

    # Assert that the function has transformed the column as expected
    assert result_df['column_name'].tolist() == [0, 1, 2, 0, 1]

if __name__ == '__main__':
    pytest.main()