import pytest
from src_0659 import task_func
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

# Mock data for testing
texts = [
    "Hello, world! This is a test.",
    "Another example, with different words.",
    "Punctuation should be removed, and stopwords too."
]

# Expected output for the mock data
expected_output = pd.DataFrame({
    'example': [1, 1, 0],
    'different': [0, 1, 0],
    'hello': [1, 0, 0],
    'is': [0, 0, 0],
    'punctuation': [0, 0, 1],
    'removed': [0, 0, 1],
    'should': [0, 0, 1],
    'test': [1, 0, 0],
    'this': [0, 0, 0],
    'with': [0, 0, 0],
    'world': [1, 0, 0]
})

def test_task_func():
    result = task_func(texts)
    # Check if the result is a DataFrame
    assert isinstance(result, pd.DataFrame)
    # Check if the columns match the expected output
    assert set(result.columns) == set(expected_output.columns)
    # Check if the shape of the result matches the expected output
    assert result.shape == expected_output.shape
    # Check if the values in the DataFrame match the expected output
    pd.testing.assert_frame_equal(result.sort_index(axis=1), expected_output.sort_index(axis=1))

if __name__ == "__main__":
    pytest.main()