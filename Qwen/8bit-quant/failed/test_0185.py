import pytest
from src_0185 import task_func
import pandas as pd

@pytest.fixture
def sample_dataframe():
    data = {
        'text': [
            "This is a sample text with numbers 123 and punctuation!",
            "Another example, with different words.",
            "Pandas and pytest are great tools."
        ]
    }
    return pd.DataFrame(data)

def test_task_func(sample_dataframe):
    result_df = task_func(sample_dataframe, 'text')
    
    # Check if the output is a DataFrame
    assert isinstance(result_df, pd.DataFrame), "The result should be a pandas DataFrame"
    
    # Check if the number of rows in the result matches the input DataFrame
    assert len(result_df) == len(sample_dataframe), "The number of rows in the result should match the input DataFrame"
    
    # Check if the DataFrame has the correct columns
    expected_columns = ['sample', 'text', 'with', 'numbers', 'punctuation', 'example', 'different', 'words', 'tools']
    assert list(result_df.columns) == expected_columns, "The DataFrame should have the correct columns"
    
    # Check if there are no NaN values in the result
    assert not result_df.isnull().values.any(), "The result should not contain any NaN values"

def test_task_func_empty_dataframe():
    empty_df = pd.DataFrame(columns=['text'])
    result_df = task_func(empty_df, 'text')
    
    # Check if the output is a DataFrame
    assert isinstance(result_df, pd.DataFrame), "The result should be a pandas DataFrame"
    
    # Check if the DataFrame is empty
    assert result_df.empty, "The result should be an empty DataFrame"
    
    # Check if the DataFrame has no columns
    assert len(result_df.columns) == 0, "The DataFrame should have no columns"