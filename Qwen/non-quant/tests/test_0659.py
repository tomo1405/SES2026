import pytest
from src_0659 import task_func
import pandas as pd

@pytest.fixture
def sample_texts():
    return [
        "Hello, world! This is a test.",
        "Python is great; isn't it?",
        "NLTK and sklearn are powerful libraries."
    ]

@pytest.fixture
def expected_output():
    # Expected output DataFrame after processing the sample_texts
    data = {
        'hello': [1, 0, 0],
        'world': [1, 0, 0],
        'this': [1, 0, 0],
        'is': [1, 1, 0],
        'a': [1, 0, 0],
        'test': [1, 0, 0],
        'python': [0, 1, 1],
        'great': [0, 1, 0],
        'isnt': [0, 1, 0],
        'it': [0, 1, 0],
        'nltk': [0, 0, 1],
        'and': [0, 0, 1],
        'sklearn': [0, 0, 1],
        'are': [0, 0, 1],
        'powerful': [0, 0, 1],
        'libraries': [0, 0, 1]
    }
    return pd.DataFrame(data)

def test_task_func(sample_texts, expected_output):
    result = task_func(sample_texts)
    # Check if the resulting DataFrame has the same columns as the expected DataFrame
    assert set(result.columns) == set(expected_output.columns)
    # Check if the resulting DataFrame has the same shape as the expected DataFrame
    assert result.shape == expected_output.shape
    # Check if the resulting DataFrame values match the expected DataFrame values
    assert result.equals(expected_output)