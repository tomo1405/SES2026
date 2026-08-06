import pandas as pd
import pytest
from src_0185 import task_func

@pytest.fixture
def dataframe():
    return pd.DataFrame({
        'text_column': ['This is a test', 'Another test to try']
    })

def test_task_func(dataframe):
    result = task_func(dataframe, 'text_column')
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (2, 104)  # 104 is the number of unique words after preprocessing
    assert all(result.columns == vectorizer.get_feature_names_out())

def test_preprocess_text():
    text = 'This is a test! 123'
    expected_result = 'this is a test'
    result = task_func.preprocess_text(text)
    assert result == expected_result