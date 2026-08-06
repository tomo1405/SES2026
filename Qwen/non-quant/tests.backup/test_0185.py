import pytest
from src_0185 import task_func
import pandas as pd

@pytest.fixture
def sample_dataframe():
    data = {
        'text': [
            'This is a sample text with numbers 123 and punctuation!',
            'Another example, with different words.',
            'Pandas and pytest are great tools for data processing.'
        ]
    }
    return pd.DataFrame(data)

def test_task_func(sample_dataframe):
    # Expected output after preprocessing and vectorization
    expected_columns = [
        'ample', 'sample', 'text', 'with', 'numbers', 'punctuation', 
        'another', 'example', 'different', 'words', 
        'pandas', 'pytest', 'great', 'tools', 'data', 'processing'
    ]
    
    result_df = task_func(sample_dataframe, 'text')
    
    # Check if the resulting DataFrame has the correct shape
    assert result_df.shape == (3, len(expected_columns))
    
    # Check if the resulting DataFrame has the correct columns
    assert all(col in result_df.columns for col in expected_columns)
    
    # Check if the resulting DataFrame contains non-negative values only
    assert (result_df >= 0).all().all()

def test_task_func_empty_dataframe():
    empty_df = pd.DataFrame(columns=['text'])
    result_df = task_func(empty_df, 'text')
    
    # Check if the resulting DataFrame is empty
    assert result_df.empty

def test_task_func_no_text_column():
    data = {'not_text': ['some', 'data']}
    df = pd.DataFrame(data)
    
    with pytest.raises(KeyError):
        task_func(df, 'text')

def test_task_func_duplicate_texts(sample_dataframe):
    sample_dataframe.loc[1, 'text'] = sample_dataframe.loc[0, 'text']
    result_df = task_func(sample_dataframe, 'text')
    
    # Check if the resulting DataFrame has the correct shape
    assert result_df.shape == (3, 11)  # Assuming 11 unique words after preprocessing
    
    # Check if the resulting DataFrame has the correct columns
    expected_columns = ['ample', 'sample', 'text', 'with', 'numbers', 'punctuation', 
                        'another', 'example', 'different', 'words', 
                        'pandas', 'pytest', 'great', 'tools', 'data', 'processing']
    assert all(col in result_df.columns for col in expected_columns)
    
    # Check if the resulting DataFrame contains non-negative values only
    assert (result_df >= 0).all().all()